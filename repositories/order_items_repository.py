import os
import mysql.connector
from mysql.connector import Error

def bulk_insert_order_items(order_items_df):
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
            INSERT INTO order_items (order_id, product_id, quantity, price)
            VALUES (%s, %s, %s, %s)
            """

            order_items_data = order_items_df.to_records(index=False).tolist()
            
            cursor.executemany(query, order_items_data)
            
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