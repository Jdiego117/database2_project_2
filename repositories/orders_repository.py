import os
import mysql.connector
from mysql.connector import Error
from common.sql_getter import sql_get

def bulk_insert_orders(orders_df):
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
            INSERT INTO orders (customer_id, total)
            VALUES (%s, %s)
            """

            orders_data = orders_df.to_records(index=False).tolist()
            
            cursor.executemany(query, orders_data)
            
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
            
def get_orders_customer():
    orders = sql_get("""
        SELECT o.id AS order_id, c.name AS customer_name, o.total
        FROM orders o
        INNER JOIN customers c ON o.customer_id = c.id;
    """)
    
    return orders

def get_orders_item_count():
    orders = sql_get("""
        SELECT o.id AS order_id, SUM(oi.quantity) AS total_items
        FROM orders o
        INNER JOIN order_items oi ON o.id = oi.order_id
        GROUP BY o.id;
    """)
    
    return orders

def get_orders_total():
    orders = sql_get("""
        SELECT SUM(total) AS total_value_of_orders
        FROM orders;
    """)
    
    return orders

def get_avg_quantity_per_order():
    orders = sql_get("""
        SELECT AVG(quantity) AS avg_quantity_per_order
        FROM order_items;
    """)
    
    return orders

def orders_details():
    orders = sql_get("""
        SELECT o.id AS order_id, c.name AS customer_name, o.total, COUNT(oi.id) AS total_items
        FROM orders o
        INNER JOIN customers c ON o.customer_id = c.id
        INNER JOIN order_items oi ON o.id = oi.order_id
        GROUP BY o.id;
    """)
    
    return orders