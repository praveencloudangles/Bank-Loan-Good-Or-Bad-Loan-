import pandas as pd

def data_loading():
    data = pd.read_csv("Bank Loan.csv")
    print(data)

    return data

data_loading()