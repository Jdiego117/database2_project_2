import os
import mysql.connector
from mysql.connector import Error
from common.sql_getter import sql_get

def bulk_insert_products(products_df):
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
            INSERT INTO products (name, price, stock_quantity)
            VALUES (%s, %s, %s)
            """

            products_data = products_df.to_records(index=False).tolist()
            
            cursor.executemany(query, products_data)
            
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
            
def products_avg_price():
    product = sql_get("""
        SELECT AVG(price) AS average_price
        FROM products;           
    """)

    return product

def products_min_price():
    product = sql_get("""
        SELECT MIN(price) AS min_product_price
        FROM products;    
    """)

    return product

def products_supplier_quantity():
    products = sql_get("""
        SELECT p.name AS product_name, p.stock_quantity, s.name AS supplier_name
        FROM products p
        LEFT JOIN product_suppliers ps ON p.id = ps.product_id
        LEFT JOIN suppliers s ON ps.supplier_id = s.id;   
    """)

    return products

def products_out_of_stock():
    products = sql_get("""
        SELECT name AS product_name
        FROM products
        WHERE stock_quantity = 0; 
    """)

    return products