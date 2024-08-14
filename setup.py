import mysql.connector

# Connect to MySQL server (replace with your own connection details)
conn = mysql.connector.connect(host="localhost",user="root",passwd="1413342")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a new database
database_name = "school2"
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

# Switch to the newly created database
cursor.execute(f"USE {database_name}")

# Create a new table within the database
table_name = "maindata"
create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (Rollno INT ,Name TEXT,Phone bigint,Email text)"
cursor.execute(create_table_query)

conn.commit()
conn.close()
