import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (no database yet)
        connection = mysql.connector.connect(
            host="localhost",     # adjust if your server is elsewhere
            user="root",          # replace with your MySQL username
            password=""           # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
