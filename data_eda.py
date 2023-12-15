#This file will extract the data and perform a basic EDA
#%%
import pandas as pd
import connect_MySQL
import matplotlib.pyplot as plt
import seaborn as sns

#%%
#Connect to my SQL database and read the data into a pandas dataframe 
#JOB : Pandas prefers SQLAlchemy engine or Database string URL or sqlite3 DBAPI connections 
pw = "######"
db = "credit_risk_taiwan"
db_connection = connect_MySQL.create_database_connection("localhost", "root", pw, db)
query = 'SELECT * FROM creditrisk'
df = pd.read_sql(query, db_connection)
# %%
#Understanding the categorical variables

#