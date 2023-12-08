#Import the dataset
#taken from mortgage data  - http://www.creditriskanalytics.net/datasets-private2.html

'''
◾ id: Borrower ID
◾ time: Time stamp of observation
◾ orig_time: Time stamp for origination
◾ first_time: Time stamp for first observation
◾ mat_time: Time stamp for maturity
◾ balance_time: Outstanding balance at observation time
◾ LTV_time: Loan-to-value ratio at observation time, in %
◾ interest_rate_time: Interest rate at observation time, in %
◾ hpi_time: House price index at observation time, base year = 100
◾ gdp_time: Gross domestic product (GDP) growth at observation time, in %
◾ uer_time: Unemployment rate at observation time, in %
◾ REtype_CO_orig_time: Real estate type condominium = 1, otherwise = 0
◾ REtype_PU_orig_time: Real estate type planned urban development = 1, otherwise = 0
◾ REtype_SF_orig_time: Single-family home = 1, otherwise = 0
◾ investor_orig_time: Investor borrower = 1, otherwise = 0
◾ balance_orig_time: Outstanding balance at origination time
◾ FICO_orig_time: FICO score at origination time, in %
◾ LTV_orig_time: Loan-to-value ratio at origination time, in %
◾ Interest_Rate_orig_time: Interest rate at origination time, in %
◾ hpi_orig_time: House price index at origination time, base year = 100
◾ default_time: Default observation at observation time
◾ payoff_time: Payoff observation at observation time
◾ status_time: Default (1), payoff (2), and nondefault/nonpayoff (0) observation at observation time
'''

#%%
import pandas as pd
import seaborn as sns

df = pd.read_csv('./data_raw/mortgage.csv')
df.head()

#%%
df.columns
# %%
