#Import the dataset
#taken from mortgage data  - http://www.creditriskanalytics.net/datasets-private2.html

import pandas as pd

df = pd.read_csv('./data_raw/mortgage.csv')
df.head()