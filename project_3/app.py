from flask import Flask
import mysql.connector
from mysql.connector import Error
import time  # Import time for the sleep function

app = Flask(__name__)

# Updated function with retry mechanism
def get_db_connection():
    retries = 5  # Number of retries
    for i in range(retries):
        try:
            connection = mysql.connector.connect(
                host="db",
                user="root",
                password="example",
                database="test_db"
            )
            return connection
        except Error as e:
            print(f"Error: {e}, retrying in 5 seconds...")
            time.sleep(5)  # Wait for 5 seconds before retrying
    return None  # Return None if the connection fails after all retries

@app.route('/')
def hello_world():
    connection = get_db_connection()

    if connection is None:
        return "Error connecting to the database"

    cursor = connection.cursor()
    cursor.execute("SELECT 'Hello, Docker!'")
    result = cursor.fetchone()
    connection.close()

 
