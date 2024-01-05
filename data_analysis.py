from data_loading import data_loading

def analysis():
    data=data_loading()
    print(data)
    print("null values-------", data.isnull().sum())
    print("duplicate values--------", data.duplicated().sum())
    print("unique values---------", data.nunique())
    print("describe-----------", data.describe())

    return data
analysis()