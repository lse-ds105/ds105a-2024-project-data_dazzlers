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

# Smithsonian 