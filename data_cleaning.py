from data_analysis import analysis

def data_cleaning():
    data = analysis()

    df = data.drop(['id','issue_d','final_d',
                'home_ownership','income_category',
                'term','application_type', 'purpose',
                'loan_condition','interest_payments',
                'grade','region'], axis=1)
    
    print("final dataframe----------------------", df)

    print(df.columns.tolist())
    
    return df

data_cleaning()