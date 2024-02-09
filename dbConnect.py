 # pip install mysql-connector-python -  install packege 
import mysql.connector

query="CREATE TABLE users(name VARCHAR(200),age INT);"
try:
    connection=mysql.connector.connect(host='localhost',database='python',user='root',password='')
    cursor=connection.cursor()
    cursor.execute(query)

    connection.commit()
except:
    print('database not connected')
finally:
    if connection.is_connected():
        connection.close()