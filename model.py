#%%
import data_cleaning_eda
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_auc_score, confusion_matrix, roc_curve, auc


#Get cleaned data
df = data_cleaning_eda.get_clean_data()


# %%
