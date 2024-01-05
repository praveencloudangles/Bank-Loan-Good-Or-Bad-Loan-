from data_cleaning import data_cleaning
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

def feat_eng():
    data = data_cleaning()
    print("--------------------",data["loan_condition_cat"].value_counts())
    x = data.drop('loan_condition_cat', axis=1)
    y = data['loan_condition_cat']
    oversample = SMOTE()
    # undersample = RandomUnderSampler()
    X, Y = oversample.fit_resample(x, y)
    data = pd.concat([X, pd.Series(Y, name='loan_condition_cat')], axis=1)
    print("after-------------------",data['loan_condition_cat'].value_counts())

    print("null values----------", data.dtypes)

    data.to_csv("bank_loan.csv")

    return data

feat_eng()