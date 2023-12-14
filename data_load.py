
import connect_MySQL
import pandas as pd
import csv

#Connect to the database in my localhost My SQL server
#Password can be set in environment variables
pw = "xxxxx"
db = "credit_risk_taiwan"

#Establish a server connections
server_connection = connect_MySQL.create_server_connection("localhost", "root", pw)

#Create a database called credit_risk_taiwan
connect_MySQL.create_database(server_connection, db)

#Check the database
connect_MySQL.check_database(server_connection)

#Connect to the database and return a new connection object
db_connection = connect_MySQL.create_database_connection("localhost", "root", pw, db)

#Query statment for creating the data scheme for credit risk taiwan data obtained from UCI-ML repo
#Multi-line strings - triple quote notation
#Make sure the variable names are not in double quotes when the query in triple quote notation
create_table_query = """
CREATE TABLE creditrisk 
(
    ID INT,
    LIMIT_BAL INT,
    SEX VARCHAR(512),
    EDUCATION INT,
    MARRIAGE INT,
    AGE INT,
    PAY_0 VARCHAR(512),
    PAY_2 VARCHAR(512),
    PAY_3 VARCHAR(512),
    PAY_4 VARCHAR(512),
    PAY_5 VARCHAR(512),
    PAY_6 VARCHAR(512),
    BILL_AMT1 INT,
    BILL_AMT2 INT,
    BILL_AMT3 INT,
    BILL_AMT4 INT,
    BILL_AMT5 INT,
    BILL_AMT6 INT,
    PAY_AMT1 INT,
    PAY_AMT2 INT,
    PAY_AMT3 INT,
    PAY_AMT4 INT,
    PAY_AMT5 INT,
    PAY_AMT6 INT,
    DEF_PAY_NEXT_MON VARCHAR(512)
);
"""

#Create a table in the connected database using the above schema
connect_MySQL.execute_query(db_connection, create_table_query) # Execute our defined query
#Add data to the empty table created using the csv file in ./data_raw
#JOB : Use sql alchemy to create a connectio engine and do his more efficiently

# Open and read the file as a single buffer
#https://stackoverflow.com/questions/19472922/reading-external-sql-script-in-python
fd = open('add_data.sql', 'r')
sqlFile = fd.read()
fd.close()

# all SQL commands (split on ';')
sqlinsertqueries = sqlFile.split(';')

for insertq in sqlinsertqueries:
    connect_MySQL.execute_query(db_connection, insertq)


#CLose connection to server
db_connection.close()

