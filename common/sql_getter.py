import os
import mysql.connector
from mysql.connector import Error

def sql_get(query, params=None):
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

            cursor.execute(query, params)
            data = cursor.fetchall()
            
    except Error as e:
        print(f"Error while getting courses from database: {e}")
    finally:
        cursor.close()
        connection.close()
        return data
