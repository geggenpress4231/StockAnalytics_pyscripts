import pyodbc

def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=MIREMS\\SQLEXPRESS;'
        'DATABASE=StockAnalytics;'
        'Trusted_Connection=yes;'
    )
    return conn
