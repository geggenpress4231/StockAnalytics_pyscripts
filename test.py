from db_connection import get_db_connection
from api import fetch_data
from insert_data import insert_data
import json

def test_db_connection():
    print("Testing database connection...")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        conn.close()
        print("Database connection successful.")
    except Exception as e:
        print(f"Database connection failed: {e}")

def test_data_fetch(symbol="IBM"):
    print(f"Testing data fetch for symbol: {symbol}...")
    data = fetch_data(symbol)
    if data:
        print("Data fetch successful.")
      
        print(json.dumps(data, indent=4)[:500])  
    else:
        print("Data fetch failed.")

def test_data_insert(symbol="IBM"):
    print("Testing data insertion...")
    try:
        conn = get_db_connection()
        data = fetch_data(symbol)
        if data:
            insert_data(conn, symbol, data)
            print("Data insertion successful.")
        else:
            print("Data fetch failed, so data insertion was not attempted.")
        conn.close()
    except Exception as e:
        print(f"Data insertion failed: {e}")

if __name__ == "__main__":
    # Run individual tests
    test_db_connection()
    test_data_fetch()
    test_data_insert()
