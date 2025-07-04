import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ninu@180161",
        database="taskdb"
    )
    return connection
