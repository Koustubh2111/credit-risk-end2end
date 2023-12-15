#This file will extract the data and perform a basic EDA
#%%
import pandas as pd
import connect_MySQL
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics import mosaicplot

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
#SEX, EDUCATION AND MARRIAGE ARE THE THREE CATEGORICAL VARIABLES
#JOB: Plot the histograms of the three categorical variables using a mosaic plot


#Raising custom exception class
class MyException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

#Distributions of the three categorical variables
def plot_vars(col_list, type):
    if type not in ['cat', 'num']:
        raise MyException("Error: Please specify the type of variable as 'cat' or 'num' as the second argument")
    fig, ax = plt.subplots(figsize = (5,5*len(col_list)),nrows=len(col_list), ncols=1)
    if type=='cat':
        for a,col in zip(ax, col_list):
            df.groupby(col).size().plot(kind='bar', ax = a)
    elif type=='num':
        for a,col in zip(ax,col_list):
            sns.histplot(df[col], ax=a)

#%%
plot_vars(['SEX', 'EDUCATION', 'MARRIAGE'], 'cat')
#%%
plot_vars(['PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', \
           'PAY_5', 'PAY_6'], type='num')
#%%
plot_vars(['BILL_AMT1', 'BILL_AMT2','BILL_AMT3', 'BILL_AMT4',\
            'BILL_AMT5', 'BILL_AMT6'], type='num')
#%%
plot_vars(['PAY_AMT1','PAY_AMT2', 'PAY_AMT3', \
           'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6'], type='num')
# %%
# %%
#Plot Output
df.groupby('DEF_PAY_NEXT_MON').size().plot(kind='bar')
# %%
