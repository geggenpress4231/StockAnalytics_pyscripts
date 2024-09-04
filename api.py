import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def fetch_data(symbol, interval="5min", outputsize="compact"):
    # Retrieve the API key from environment variables
    API_KEY = os.getenv('API_KEY')
    
    
    if not API_KEY:
        print("API Key not found. Please set the API_KEY environment variable.")
        return None

    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize,
        "apikey": API_KEY
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Data fetched successfully at {datetime.now()}")
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Test the function
fetch_data("IBM")
