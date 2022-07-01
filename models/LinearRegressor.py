import os, pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split


class LinearRegressorModel:
    def __init__(self):
        # Instantiating a LinearRegressor Model
        self.model = LinearRegression()
        self.model_name = "LinearRegressor"

    def read_data(self, url:str, sep:str=","):
        df = pd.read_csv(url, sep=sep)
        return df

    def split_data(self, features, label, shuffle:bool=True, train_size:float=0.3, random_state=42):
        return train_test_split(features, label, shuffle=shuffle, train_size=train_size, random_state=random_state)
    
    def train_data(self, dataframe):
        X_train, X_test, y_train, y_test = dataframe
        self.model.fit(X_train, y_train)

    def predict_data(self, dataframe):
        X_train, X_test, y_train, y_test = dataframe

        # self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        return predictions

    def evaluate_data(self, y_test, predictions):
        r2   = r2_score(y_test, predictions)
        rmse = mean_squared_error(y_test, predictions)
        mae  = mean_absolute_error(y_test, predictions)

        output = [ str(i)+","+str(j) for i,j in zip(predictions, y_test) ]

        result = {"rmse":rmse, "mae":mae, "r2":r2, "output":output}
        
        return result
