#%%
import connect_MySQL
import pandas as pd
#%%
#Connect to the database in my localhost My SQL server
#Password can be set in environment variables
pw = "koustubh"
db = "credit_risk_taiwan"

#Establish a server connections
server_connection = connect_MySQL.create_server_connection("localhost", "root", pw)

#Create a database called credit_risk_taiwan
connect_MySQL.create_database(server_connection, db)

#Check the database
connect_MySQL.check_database(server_connection)

#Connect to the database and return a new connection object
db_connection = connect_MySQL.create_database_connection("localhost", "root", pw, db)
#%%
#Query statment for creating the data scheme for credit risk taiwan data obtained from UCI-ML repo
#Multi-line strings - triple quote notation
create_table_query = """
CREATE TABLE creditrisk 
(
    "ID"	INT,
    "LIMIT_BAL"	INT,
    "SEX"	VARCHAR(512),
    "EDUCATION"	INT,
    "MARRIAGE"	INT,
    "AGE"	INT,
    "PAY_0"	VARCHAR(512),
    "PAY_2"	VARCHAR(512),
    "PAY_3"	VARCHAR(512),
    "PAY_4"	VARCHAR(512),
    "PAY_5"	VARCHAR(512),
    "PAY_6"	VARCHAR(512),
    "BILL_AMT1"	INT,
    "BILL_AMT2"	INT,
    "BILL_AMT3"	INT,
    "BILL_AMT4"	INT,
    "BILL_AMT5"	INT,
    "BILL_AMT6"	INT,
    "PAY_AMT1"	INT,
    "PAY_AMT2"	INT,
    "PAY_AMT3"	INT,
    "PAY_AMT4"	INT,
    "PAY_AMT5"	INT,
    "PAY_AMT6"	INT,
    "default.payment.next.month"	VARCHAR(512)
);
"""
#%%
connect_MySQL.execute_query(db_connection, create_table_query) # Execute our defined query
# %%
