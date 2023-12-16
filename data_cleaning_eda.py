import pandas as pd
import connect_MySQL
import matplotlib.pyplot as plt
import seaborn as sns
#from statsmodels.graphics import mosaicplot

def get_data(pw,db):
    '''
    Connect to my SQL database and read the data into a pandas dataframe 
    JOB : Pandas prefers SQLAlchemy engine or Database string URL 
    or sqlite3 DBAPI connections 
    '''
    db_connection = connect_MySQL.create_database_connection("localhost", "root", pw, db)
    query = 'SELECT * FROM creditrisk'
    df = pd.read_sql(query, db_connection)
    return df

#Raising custom exception class
class MyException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

#Distributions of the three categorical variables
def plot_vars(df, col_list, type):
    '''
    Understanding the categorical variables
    SEX, EDUCATION AND MARRIAGE ARE THE THREE CATEGORICAL VARIABLES
    JOB: Plot the histograms of the three categorical variables using a mosaic plot

    '''
    if type not in ['cat', 'num']:
        raise MyException("Error: Please specify the type of variable as 'cat' or 'num' as the second argument")
    fig, ax = plt.subplots(figsize = (5,5*len(col_list)),nrows=len(col_list), ncols=1)
    if type=='cat':
        for a,col in zip(ax, col_list):
            df.groupby(col).size().plot(kind='bar', ax = a)
    elif type=='num':
        for a,col in zip(ax,col_list):
            sns.histplot(df[col], ax=a)

#Data Cleaning
def get_clean_data():

    #Obatin the data using the password and the database name 
    pw = "koustubh"
    db = "credit_risk_taiwan"
    df = get_data(pw,db)
 
    #1.Combining the '0' in marriage as '3'
    df.loc[df.MARRIAGE == 0, 'MARRIAGE'] = 3
    
    #2. Combining 0,4,5 in education to 4
    df.loc[(df.EDUCATION == 5) | (df.EDUCATION == 6) | (df.EDUCATION == 0) ,'EDUCATION'] = 4

    #Rename map
    rename_map = {'PAY_0' : 'PAY_SEPT',\
                'PAY_2' : 'PAY_AUG',\
                'PAY_3' : 'PAY_JUL',\
                'PAY_4' : 'PAY_JUN',\
                'PAY_5' : 'PAY_MAY',\
                'PAY_6' : 'PAY_APR'}
    df.rename(columns=rename_map, inplace = True)

    '''
    3. The variable PAY_X describes the number of months in pay delay
    -1=pay duly, 1=payment delay for one month, 2=payment delay for two months,
    8=payment delay for eight months, 9=payment delay for nine months and above
    PAY_0: Repayment status in September, 2005
    PAY_2: Repayment status in August, 2005
    PAY_3: Repayment status in July, 2005
    PAY_4: Repayment status in June, 2005
    PAY_5: Repayment status in May, 2005
    PAY_6: Repayment status in April, 2005

    '''
    #Any value in PAY_X below -1 is changed to 0 or Pay duly
    replace_map = {'-2' : '0', '-1' : '0'}  
    for col in ['PAY_SEPT', 'PAY_AUG', 'PAY_JUL', 'PAY_JUN', 'PAY_MAY', 'PAY_APR']:
        #JOB : Can be done more effectively 
        df[col] = df.replace({col: replace_map})[col]

    #Change dataframe to integer
    df.apply(pd.to_numeric)

    return df

