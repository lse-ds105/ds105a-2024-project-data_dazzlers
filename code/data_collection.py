# FRED API

import os
import json
import requests

import pandas as pd

from dotenv import load_dotenv
from tqdm.notebook import tqdm
tqdm.pandas()

from IPython.display import Image

def get_GDP_data(api_key, start_date, end_date, sort_order='desc', file_type='json'):
    """
    Fetch GDP data from the FRED API.

    Parameters:
    - api_key (str): FRED API key.
    - start_date (str): The start date for the data (YYYY-MM-DD).
    - end_date (str): The end date for the data (YYYY-MM-DD).
    - sort_order (str): The order of the data based on observation date.
    - file_type (str): The format for the data.

    Returns:
    - list: A list of GDP data observations.
    """

    url = 'https://api.stlouisfed.org/fred/series/observations'

    params = {
        'series_id': 'GDPCA',
        'api_key': api_key,          
        'file_type': file_type,      
        'sort_order': sort_order,    
        'observation_start': start_date,  
        'observation_end': end_date  
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['observations']
    else:
        return f"Error: {response.status_code} - {response.text}"


# GDELT

import requests
import zipfile
import io
import os
import pandas as pd
import time
from datetime import datetime
import warnings

import json
import glob
import datetime

from dotenv import load_dotenv
from tqdm.notebook import tqdm
tqdm.pandas()

from IPython.display import Image

import sqlite3
from sqlalchemy import create_engine, text


def download_and_process_zip(url, output_dir, retries=3, delay=2):
    """
    Downloads and processes a zip file, adding column headers, filtering for US protest events, 
    and returns a filtered DataFrame.
    
    Args:
        url (str): URL of the GDELT zip file.
        output_dir (str): Directory to store the extracted files.
        retries (int): Number of retry attempts on failure.
        delay (int): Delay (in seconds) between retries.
        
    Returns:
        pd.DataFrame: Processed data, or None if the download failed.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_name = url.split("/")[-1]
    zip_path = os.path.join(output_dir, file_name)

    # Try to download the file with retries
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 404:
                print(f"File not found (404): {url}")
                return None
            elif response.status_code == 200:
                with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                    # Extract the first file from the zip
                    for file in z.namelist():
                        with z.open(file) as csv_file:
                            # Read the CSV file into a DataFrame without headers
                            df = pd.read_csv(csv_file, sep='\t', header=None, low_memory=False)
                            
                            # Check the number of columns and adjust headers accordingly
                            num_columns = df.shape[1]
                            if num_columns == len(GDELT_COLUMNS):
                                df.columns = GDELT_COLUMNS
                            else:
                                print(f"Warning: Column mismatch. Expected {len(GDELT_COLUMNS)} columns, but found {num_columns}.")
                            
                            # Filter for US protest events only 
                            df_filtered = df[(df['Actor1Geo_CountryCode'] == 'US') & (df['EventCode'] == 140)]
                            return df_filtered
            else:
                print(f"Failed to download {url}. HTTP Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")
        
        print(f"Retrying in {delay} seconds...")
        time.sleep(delay)

    print(f"Failed to download after {retries} attempts: {url}")
    return None

def process_year_data(start_year, end_year, output_dir=".../../data/raw"):
    """
    Processes data for the entire year, one zip file at a time, and saves the result as a single CSV.
    
    Args:
        start_year (int): Start year for the data.
        end_year (int): End year for the data.
        output_dir (str): Directory to store the extracted and processed data.
    """
    for year in range(start_year, end_year + 1):
        print(f"Processing data for year {year}...")
        year_data = pd.DataFrame()  # To store processed data for the year

        # Process each day in the year
        for month in range(1, 13):  # Loop over each month
            for day in range(1, 32):  # Loop over each day
                # Build the URL for the daily file (assuming the GDELT format is daily post 2013)
                url = f"http://data.gdeltproject.org/events/{year}{str(month).zfill(2)}{str(day).zfill(2)}.export.CSV.zip"
                
                # Download and process the zip file
                df_filtered = download_and_process_zip(url, output_dir)
                if df_filtered is not None:
                    # Concatenate the filtered data for the day into the year's dataframe
                    year_data = pd.concat([year_data, df_filtered], ignore_index=True)
                
                # Add a small delay between requests
                time.sleep(2)

        # Save the year's data to a CSV file
        if not year_data.empty:
            output_file = os.path.join(output_dir, f"{year}_protest_data.csv")
            year_data.to_csv(output_file, index=False)
            print(f"Year {year} data saved to {output_file}")
        else:
            print(f"No data found for year {year}.")


def download_and_process_monthly_zip(url, output_dir):
    """
    Downloads and processes a monthly GDELT zip file, filters for US social movement data, 
    and returns a DataFrame.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_name = url.split("/")[-1]
    zip_path = os.path.join(output_dir, file_name)

    try:
        response = requests.get(url, timeout=60)
        if response.status_code == 404:
            print(f"File not found (404): {url}")
            return None
        elif response.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                for file in z.namelist():
                    with z.open(file) as csv_file:
                        # Read in chunks to handle large files
                        chunk_list = []
                        for chunk in pd.read_csv(csv_file, sep='\t', header=None, low_memory=True, chunksize=100000):
                            chunk.columns = GDELT_COLUMNS[:chunk.shape[1]]
                            filtered_chunk = chunk[(chunk['Actor1Geo_CountryCode'] == 'US') & (chunk['EventCode'] == 140)]
                            chunk_list.append(filtered_chunk)
                        if chunk_list:
                            return pd.concat(chunk_list, ignore_index=True)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    except zipfile.BadZipFile as e:
        print(f"Zip file error: {e}")
    return None
    

def Process_year_data(start_year, end_year, output_dir="../../data/raw"):
    """
    Processes data from 2006 to 2013, combining monthly files into yearly CSVs.
    """
    for year in range(start_year, end_year + 1):
        print(f"Processing data for year {year}...")
        year_data = pd.DataFrame()  # Initialize yearly data storage

        for month in range(1, 13):
            # Build the URL for the monthly file
            url = f"http://data.gdeltproject.org/events/{year}{str(month).zfill(2)}.zip"
            
            # Download and process the monthly file
            df_filtered = download_and_process_monthly_zip(url, output_dir)
            if df_filtered is not None:
                year_data = pd.concat([year_data, df_filtered], ignore_index=True)

            # Add a delay to avoid overloading the server
            time.sleep(2)

        # Save the year's data to a CSV file
        if not year_data.empty:
            output_file = os.path.join(output_dir, f"{year}_protest_data.csv")
            year_data.to_csv(output_file, index=False)
            print(f"Year {year} data saved to {output_file}")
        else:
            print(f"No data found for year {year}.")


# Smithsonian 
import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd
import time
from collections import Counter



def category_search(q=None, category=None, start=0, rows=10, sort='relevancy', api_key=None):
    """
    Fetches content based on a query against a category. art_design, history_culture or science_technology.
    """
    sort_vals = ["relevancy", "id", "newest", "updated", "random"]
    if sort not in sort_vals:
        raise ValueError("Allowed values for '{}' are: {}".format("sort", ', '.join(sort_vals)))
    category_vals = ["art_design", "history_culture", "science_technology"]
    if category not in category_vals:
        raise ValueError("Allowed values for '{}' are: {}".format("category", ', '.join(category_vals)))
    if q is None:
        raise ValueError("'q' value is required.")
    start = int(start)
    rows = int(rows)
    if api_key is None:
        raise ValueError("'api_key' value is required. Please register with https://api.data.gov/signup/ to get a key.")
    search_url = "https://api.si.edu/openaccess/api/v1.0/category/{}/search?q={}&start={}&rows={}&sort={}&api_key={}".format(category, q, start, rows, sort, api_key)
    response = requests.get(search_url)
    # Check if API returned an error:
    if response.status_code != 200:
        raise Exception("API returned error: {} (code: {})".format(response.reason, response.status_code))
    res = json.loads(response.text)
    if res['response']['rowCount'] == 0:
        return None
    else:
        return res['response']['rows']

def fetch_large_artwork_dataset(api_key, query="art", category="art_design", max_results=20000, batch_size=100):
    """
    Fetches a large dataset of artworks from the Smithsonian API, including production dates and themes.

    Args:
        api_key (str): Your Smithsonian API key.
        query (str): Search query (e.g., "American art").
        category (str): Category to search within (default is "art_design").
        max_results (int): Maximum number of results to fetch.
        batch_size (int): Number of results to fetch per request.

    Returns:
        list: List of dictionaries containing artwork metadata, themes, and production dates.
    """
    all_results = []
    for start in range(0, max_results, batch_size):
        print(f"Fetching records {start} to {start + batch_size}...")
        try:
            rows = category_search(
                q=query,
                category=category,
                start=start,
                rows=batch_size,
                sort="relevancy",
                api_key=api_key,
            )
            if rows is None:
                break
            # Extract relevant fields
            for row in rows:
                content = row.get("content", {})
                indexed_structured = content.get("indexedStructured", {})
                descriptive_non_repeating = content.get("descriptiveNonRepeating", {})
                data = {
                    "id": row.get("id"),
                    "title": row.get("title"),
                    "type": descriptive_non_repeating.get("data_source"),
                    "topic": indexed_structured.get("topic", []),
                    "production_date": indexed_structured.get("date", []),  # Date when artwork was produced
                    "online_media": descriptive_non_repeating.get("online_media"),
                }
                all_results.append(data)
        except Exception as e:
            print(f"Error fetching data: {e}")
            break
        
        # Break loop early if we reach the max results
        if len(all_results) >= max_results:
            break
    
    print(f"Total records fetched: {len(all_results)}")
    return all_results[:max_results]


def save_json(data, filepath):
    """
    Saves data to a JSON file.

    Args:
        data (list): List of dictionaries to save.
        filepath (str): Path to save the JSON file.
    """
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filepath}")


def extract_year_from_date(production_date):
    """
    Extracts the year from a production date string if possible.

    Args:
        production_date (str): The production date.

    Returns:
        int or None: Extracted year if present, else None.
    """
    if isinstance(production_date, str):
        for part in production_date.split():
            if part.isdigit() and len(part) == 4:  # Check if it's a 4-digit year
                return int(part)
    return None

def extract_and_visualize_art_data(json_filepath):
    """
    Extracts themes and production years from JSON data and visualizes them.

    Args:
        json_filepath (str): Path to the JSON file.

    Returns:
        pd.DataFrame: DataFrame with processed artwork data.
    """
    with open(json_filepath, "r") as f:
        data = json.load(f)
    
    # Flatten the data into a DataFrame
    rows = []
    for item in data:
        production_year = extract_year_from_date(item.get("production_date", []))
        row = {
            "ID": item.get("id"),
            "Title": item.get("title"),
            "Type": item.get("type"),
            "ProductionDate": production_year,
            "Topics": ", ".join(item.get("topic", [])),
        }
        rows.append(row)
    df = pd.DataFrame(rows)
    
    return df


def visualize_art_trends(yearly_theme_counts, top_n=10):
    """
    Visualizes trends in art themes over time.
    
    Parameters:
        yearly_theme_counts (pd.DataFrame): DataFrame with yearly theme counts.
        top_n (int): Number of top themes to visualize based on total count.
    """
    # Identify top N themes by overall count
    top_themes = (
        yearly_theme_counts.groupby("Theme")["Count"]
        .sum()
        .nlargest(top_n)
        .index
    )
    
    # Filter the data to include only the top themes
    filtered_data = yearly_theme_counts[yearly_theme_counts["Theme"].isin(top_themes)]
    
    # Set up the plot
    plt.figure(figsize=(14, 8))
    sns.lineplot(
        data=filtered_data,
        x="Year",
        y="Count",
        hue="Theme",
        marker="o"
    )
    
    # Customizing the plot
    plt.title("Trends in Art Themes Over Time (1900 Onwards)", fontsize=16)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Count of Artworks", fontsize=14)
    plt.legend(title="Theme", title_fontsize=12, fontsize=10, loc='upper left')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    
    # Show the plot
    plt.show()



def visualize_theme_distribution(theme_counts, top_n=10):
    """
    Visualizes the distribution of top themes.
    
    Parameters:
        theme_counts (pd.DataFrame): DataFrame with total theme counts.
        top_n (int): Number of top themes to display.
    """
    # Get the top N themes
    top_theme_counts = theme_counts.nlargest(top_n, "Count")
    
    # Set up the plot
    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=top_theme_counts,
        x="Count",
        y="Theme",
        palette="viridis"
    )
    
    # Customizing the plot
    plt.title("Top Art Themes by Total Count", fontsize=16)
    plt.xlabel("Total Count", fontsize=14)
    plt.ylabel("Theme", fontsize=14)
    plt.tight_layout()
    
    # Show the plot
    plt.show()


def top_themes_per_decade(yearly_theme_counts):
    """
    Identifies the top 3 themes per decade based on their total count.
    
    Parameters:
        yearly_theme_counts (pd.DataFrame): DataFrame with columns 'Year', 'Theme', and 'Count'.
    
    Returns:
        pd.DataFrame: DataFrame with top 3 themes per decade.
    """
    # Convert Year to int and calculate the Decade
    yearly_theme_counts['Decade'] = (yearly_theme_counts['Year'] // 10) * 10
    
    # Group by Decade and Theme, then sum the counts
    decade_theme_counts = (
        yearly_theme_counts.groupby(['Decade', 'Theme'])['Count']
        .sum()
        .reset_index()
    )
    
    # Rank themes within each decade and select the top 3
    decade_theme_counts['Rank'] = (
        decade_theme_counts.groupby('Decade')['Count']
        .rank(method='first', ascending=False)
    )
    top_themes = decade_theme_counts[decade_theme_counts['Rank'] <= 3]
    
    # Sort the result for better readability
    top_themes = top_themes.sort_values(by=['Decade', 'Rank']).reset_index(drop=True)
    
    return top_themes


def visualize_top_themes_per_decade(top_themes):
    """
    Visualizes the top 3 themes per decade as a bar plot.
    
    Parameters:
        top_themes (pd.DataFrame): DataFrame with columns 'Decade', 'Theme', 'Count', and 'Rank'.
    """
    # Set up the plot
    plt.figure(figsize=(14, 8))
    sns.barplot(
        data=top_themes,
        x="Decade",
        y="Count",
        hue="Theme",
        palette="viridis"
    )
    
    # Customizing the plot
    plt.title("Themes are more commonly shared before the 1940's", fontsize=16)
    plt.xlabel("Decade", fontsize=14)
    plt.ylabel("Count of Artworks", fontsize=14)
    plt.legend(title="Theme", title_fontsize=12, fontsize=10, loc='upper left')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    
    # Show the plot
    plt.show()


