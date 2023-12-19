#This code will build a workflow for the project using prefect
from prefect import task, flow
import data_cleaning_eda
import pandas as pd

#Extracting the data from the SQL server
@task
def load_data(pw,db):
    return data_cleaning_eda.get_data(pw,db)

#
  