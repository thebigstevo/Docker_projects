from flask import Flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="db",
            user="root",
            password="example",
            database="test_db"
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def hello_world():
    connection = get_db_connection()

    if connection is None:
        return "Error connecting to the database"

    cursor = connection.cursor()
    cursor.execute("SELECT 'Hello, Docker!'")
    result = cursor.fetchone()  # Corrected typo
    connection.close()

    return str(result[0])  # Return the result as a string

if __name__ == "__main__":
    app.run(host='0.0.0.0')
