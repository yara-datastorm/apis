"""
    
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def imputation_feature_colmn(dataframe, features):
    try:
        for col in features:
            # int or float
            if dataframe[col].dtype=='int64' or dataframe[col].dtype=='float64':
                moy = dataframe[col].mean()
                dataframe[col][dataframe[col].isnull()==True] = moy 
            # object
            elif dataframe[col].dtype=='object':
                mode = dataframe[col].mode()[0]
                dataframe[col][dataframe[col].isnull()==True] = mode
            else:
                continue

        return dataframe
    except Exception as ex:
        raise ('b something is wrong')


