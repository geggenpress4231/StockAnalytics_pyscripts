import time
import pyodbc  


def get_db_connection():
    try:
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=your_server_name;DATABASE=your_db_name;UID=your_username;PWD=your_password')
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


def execute_procedure(conn, procedure_name, stock_id):
    try:
        cursor = conn.cursor()
        cursor.execute(f"EXEC {procedure_name} ?", stock_id)
        conn.commit()
        print(f"Executed {procedure_name} for stock_id {stock_id}")
    except Exception as e:
        print(f"Error executing {procedure_name} for stock_id {stock_id}: {e}")


def execute_all_procedures_for_stock(conn, stock_id):
    procedures = [
        'CalculateMovingAverage5',
        'CalculateMovingAverage10',
        'CalculateRSI',
        'CalculateMACD',
        'CalculateBollingerBands'
    ]
    
    for procedure in procedures:
        execute_procedure(conn, procedure, stock_id)


def start_stock_parameters_scheduler():
    while True:
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT id FROM Stock")
                stock_ids = [row[0] for row in cursor.fetchall()]
                
                for stock_id in stock_ids:
                    execute_all_procedures_for_stock(conn, stock_id)

            except Exception as e:
                print(f"Error fetching stock IDs: {e}")
            finally:
                conn.close()
        
      
        print("Waiting for the next hour...")
        time.sleep(3600)

if __name__ == "__main__":
    start_stock_parameters_scheduler()
