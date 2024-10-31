import os
import mysql.connector
from mysql.connector import Error
from common.sql_getter import sql_get

def bulk_insert_customers(customers_df):
    connection = None
    cursor = None
    
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            query = f"""
            INSERT INTO customers (name, email, identification)
            VALUES (%s, %s, %s)
            """

            customers_data = customers_df.to_records(index=False).tolist()
            
            cursor.executemany(query, customers_data)
            
            connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")
        if connection:
            connection.rollback()
    finally:
        if cursor is not None:
            cursor.close()
            
        if connection is not None and connection.is_connected():
            connection.close()
            
def get_customers():
    customers = sql_get("SELECT c.id, c.name, c.email, c.identification FROM customers as c")
    return customers

def get_customers_expense():
    customers = sql_get("""
        SELECT c.name AS customer_name, c.email as customer_email, SUM(o.total) AS total_spent
        FROM customers c
        LEFT JOIN orders o ON c.id = o.customer_id
        GROUP BY c.id;                    
    """)
    
    return customers

def get_customers_with_orders():
    customers = sql_get("""
        SELECT c.email AS customer_email, c.name AS customer_name, c.identification AS customer_identification, COUNT(o.id) AS order_count
        FROM customers c
        INNER JOIN orders o ON c.id = o.customer_id
        GROUP BY c.id;
    """)
    
    return customers

def get_customers_without_orders():
    customers = sql_get("""
        SELECT c.id AS customer_id, c.name AS customer_name, c.identification
        FROM customers c
        LEFT JOIN orders o ON c.id = o.customer_id
        WHERE o.id IS NULL;
    """)
    
    return customers