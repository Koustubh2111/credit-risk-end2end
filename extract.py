import mysql.connector
from mysql.connector import Error
import pandas as pd

#A fourth arg can be passed to the connect method - database name
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Server connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#Create databases in the MySQL server
#name_str is the name of the user defined database 
def create_database(connection, name_str):
    cursor = connection.cursor()
    query = "CREATE DATABASE " + name_str
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def check_database(connection):
    cursor = connection.cursor()
    query  = "SHOW DATABASES"
    try:
        cursor.execute(query)
        for d in cursor:
            print(d)
    except Error as err:
        print(f"Error: '{err}'")

def create_database_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection   









#pw = "koustubh"
#connection = create_server_connection("localhost", "root", pw)