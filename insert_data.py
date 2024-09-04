import requests
import pyodbc
from datetime import datetime
import os

def fetch_latest_data(symbol, interval="5min"):
    API_KEY = os.getenv('API_KEY')
    
    if not API_KEY:
        print("API Key not found. Please set the API_KEY environment variable.")
        return None

    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "outputsize": "compact",
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

def insert_data(conn, symbol, data):
    time_series = data.get("Time Series (5min)", {})
    latest_time = max([datetime.strptime(time, "%Y-%m-%d %H:%M:%S") for time in time_series.keys()])
    
    cursor = conn.cursor()
    latest_data = time_series[str(latest_time)]
    open_price = float(latest_data["1. open"])
    close_price = float(latest_data["4. close"])
    
 
    cursor.execute("""
        INSERT INTO Stock (symbol, timestamp, open_price, close_price)
        VALUES (?, ?, ?, ?)
    """, (symbol, latest_time, open_price, close_price))

    conn.commit()
    cursor.close()
    print(f"Latest data for {latest_time} inserted successfully.")

