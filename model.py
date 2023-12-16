#%%
import data_cleaning_eda
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_auc_score, confusion_matrix, roc_curve, auc
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

"""
Add methods for different models 
"""
def get_data():
    return data_cleaning_eda.get_clean_data()

def split_data(df):
    #Split into features and labels
    X = df.drop('DEF_PAY_NEXT_MON',axis=1)
    y = df['DEF_PAY_NEXT_MON']

    #Normalize 
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.33, \
                        random_state=42, stratify = y)
    return X_train, X_test, y_train, y_test
    

def logistic_regression():
    '''
    Writing a basic logistic regression function
    JOB : Feature engineer before training 
    '''
    df = get_data()

    X_train, X_test, y_train, y_test = split_data(df)

    clf = LogisticRegression(random_state=0).fit(X_train, y_train)

    train_class_preds = clf.predict(X_train)
    test_class_preds = clf.predict(X_test)


    train_accuracy_lr = accuracy_score(train_class_preds,y_train)
    test_accuracy_lr = accuracy_score(test_class_preds,y_test)

    print("The accuracy on train data is ", train_accuracy_lr)
    print("The accuracy on test data is ", test_accuracy_lr)

    test_accuracy_lr = accuracy_score(test_class_preds,y_test)
    test_precision_score_lr = precision_score(test_class_preds,y_test)
    test_recall_score_lr = recall_score(test_class_preds,y_test)
    test_f1_score_lr = f1_score(test_class_preds,y_test)
    test_roc_score_lr = roc_auc_score(test_class_preds,y_test)

    print("The accuracy on test data is ", test_accuracy_lr)
    print("The precision on test data is ", test_precision_score_lr)
    print("The recall on test data is ", test_recall_score_lr)
    print("The f1 on test data is ", test_f1_score_lr)
    print("The roc_score on test data is ", test_roc_score_lr)

