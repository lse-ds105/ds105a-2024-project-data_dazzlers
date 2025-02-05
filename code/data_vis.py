import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib as mpl
import pandas as pd
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import plotly.graph_objects as go
import colorsys
import plotly.io as pio
import sqlite3
import seaborn as sns
from sqlalchemy import create_engine
import plotly.express as px

import os
import json
import requests
import glob

from dotenv import load_dotenv
from tqdm.notebook import tqdm
tqdm.pandas()

from IPython.display import Image

from sqlalchemy import create_engine, text

#GDP and art visualisations

# Function to compute mean GDP for each decade
def get_mean_gdp_by_decade(df_gdp):
    # Convert the 'Date' column to datetime if not already in datetime format
    df_gdp['Date'] = pd.to_datetime(df_gdp['Date'])

    # Extract the decade by flooring the year to the nearest multiple of 10
    df_gdp['Decade'] = (df_gdp['Date'].dt.year // 10) * 10

    # Filter to get only data between 1920 and 2010
    df_gdp = df_gdp[df_gdp['Decade'].between(1920, 2010)]

    # Group by 'Decade' and calculate the mean GDP for each decade
    gdp_by_decade = df_gdp.groupby('Decade')['GDP_Billions'].mean().reset_index()

    return gdp_by_decade

def create_theme_array(csv_file):
    # Read the CSV file
    data = pd.read_csv(csv_file)
    
    # Extract themes (columns excluding "Decade")
    themes = list(data.columns[1:])
    
    # Extract counts as a 2D NumPy array
    theme_counts = data.iloc[:, 1:].values  
    
    return themes, theme_counts


# Function to generate high-contrast colors
def generate_colors(n):
    colors = []
    for i in range(n):
        hue = (i * 137.5) % 360  # Spread colors around the HSL wheel
        rgb = colorsys.hls_to_rgb(hue / 360, 0.4, 1.0)  # Ensure mid-brightness
        hex_color = "#{:02x}{:02x}{:02x}".format(
            int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
        )
        colors.append(hex_color)
    return colors



