import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD')
)              
cursor = connection.cursor()

if connection.is_connected():
    print("Connected to MySQL successfully!")
    
    cursor.execute("SHOW DATABASES;")
    print("DATABASE：")
    for db in cursor:
        print(" -", db[0])

# "MySQL connection is closed."
cursor.close()
connection.close()