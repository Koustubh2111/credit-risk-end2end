
#%%
#Using the quandl api for data extraction
import quandl
import pandas as pd

#Get quandl api key
quandl.ApiConfig.api_key = Nc_AkzWzznN-zUmoBHxm

#%%
quandl.get_table('ZILLOW/DATA',indicator_id='ZSFH', region_id='99999')