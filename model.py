#%%
import data_cleaning_eda
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_auc_score, confusion_matrix, roc_curve, auc
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#%%
#Get cleaned data
df = data_cleaning_eda.get_clean_data()


# %%
X = df.drop('DEF_PAY_NEXT_MON',axis=1)
Y = df['DEF_PAY_NEXT_MON']

# %%
#Split into training and test test
scaler = StandardScaler()
X = scaler.fit_transform(X)

# %%
X_train, X_test, y_train, y_test = \
    train_test_split(X, Y, test_size=0.33, \
                     random_state=42, stratify = Y)

# %%

