import time
from db_connection import get_db_connection
from api import fetch_data
from insert_data import insert_data

def scheduled_task(symbol="IBM"):
    try:
        print(f"Starting scheduled task for symbol: {symbol}...")

     
        conn = get_db_connection()
        if conn:
            print("Database connection established.")

         
            data = fetch_data(symbol)
            if data:
                print("Data fetched successfully.")

              
                insert_data(conn, symbol, data)
                print("Data inserted successfully.")
            else:
                print("Data fetch failed; data insertion skipped.")
            
         
            conn.close()
            print("Database connection closed.")
        else:
            print("Failed to establish a database connection.")
    except Exception as e:
        print(f"An error occurred during the scheduled task: {e}")

def start_scheduler(interval=600, symbol="IBM"):
    while True:
        scheduled_task(symbol)
        print(f"Task completed. Waiting for {interval / 60} minutes before the next run...\n")
        time.sleep(interval)

if __name__ == "__main__":
    start_scheduler()
