import os
import mysql.connector
from mysql.connector import Error
from common.sql_getter import sql_get

def bulk_insert_suppliers(suppliers_df):
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
            INSERT INTO suppliers (name, contact_email)
            VALUES (%s, %s)
            """

            suppliers_data = suppliers_df.to_records(index=False).tolist()
            
            cursor.executemany(query, suppliers_data)
            
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
            
def get_suppliers_products():
    suppliers = sql_get("""
        SELECT s.name AS supplier_name, COUNT(ps.product_id) AS number_of_products
        FROM suppliers s
        LEFT JOIN product_suppliers ps ON s.id = ps.supplier_id
        GROUP BY s.id;          
    """)
    
    return suppliers
