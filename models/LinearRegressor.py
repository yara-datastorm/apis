from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.staticfiles import StaticFiles

from pathlib import Path
import shutil # save upload file
import uuid


import os, pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")


class LinearRegressionModel:
    def __init__(self):
        # Instantiating a LinearRegression Model
        self.model = LinearRegression()

    def read_data(self, url:str, sep:str=","):
        df = pd.read_csv(url, sep=sep)
        return df

    def split_data(self, features, label, shuffle:bool=True, train_size:float=0.3):
        return train_test_split(features, label, shuffle=shuffle, train_size=train_size)
    
    def train_data(self, dataframe):
        X_train, X_test, y_train, y_test = dataframe
        self.model.fit(X_train, y_train)

    def predict_data(self, dataframe):
        X_train, X_test, y_train, y_test = dataframe

        # self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)

        r2 = r2_score(y_test, predictions)
        rmse = mean_squared_error(y_test, predictions, squared=False)

        output = [ str(i)+","+str(j) for i,j in zip(predictions, y_test) ]

        result = {"rmse":rmse, "r2":r2, "output":output}
        
        return result


class LogisticRegressionModel:
    def __init__(self):
        # Instantiating a LogisticRegression Model
        self.model = LogisticRegression()

    def read_data(self, url:str, sep:str=","):
        df = pd.read_csv(url, sep=sep)
        return df

    def split_data(self, features, label, shuffle:bool=True, train_size:float=0.3):
        return train_test_split(features, label, shuffle=shuffle, train_size=train_size)
    
    def train_data(self, dataframe):
        X_train, X_test, y_train, y_test = dataframe
        self.model.fit(X_train, y_train)

    def predict_data(self, dataframe):
        X_train, X_test, y_train, y_test = dataframe

        # self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)

        r2 = r2_score(y_test, predictions)
        rmse = mean_squared_error(y_test, predictions, squared=False)

        output = [ str(i)+","+str(j) for i,j in zip(predictions, y_test) ]

        result = {"rmse":rmse, "r2":r2, "output":output}
        
        return result



# home
url1 = "https://raw.githubusercontent.com/datagy/data/main/insurance.csv" # x=charges y=age
url2 = "https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/difficile.csv" # x=libido y=dose
@router.post("/")   
async def home(data_url:str=url2, features:str="dose", label:str="libido", uploaded_file:UploadFile=File(...)):
    """
    > **features:str**
    >> Variables à predire (ex: y)
    ---
    > **label:str**
    >> Variables explicatives(ex: var1,var2,...)
    """
    myuuid = uuid.uuid4()
    file_path = "static/{}#{}".format(myuuid, uploaded_file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    # print(uploaded_file)
    # print(uploaded_file.file)
    # print(uploaded_file.filename)
    # print(uploaded_file.content_type)
    # print(uploaded_file.headers)
    # print(uploaded_file.spool_max_size)
    # print(dir(uploaded_file))

    # Creating two arrays for the feature and target
    features = features.split(",")
    label = label

    my_model = LinearRegressionModel()
    # my_model = LogisticRegressionModel()
    df = my_model.read_data(url=data_url)

    X = df[features].astype(int)
    y = df[label].astype(int)

    dataframe = my_model.split_data(features=X, label=y)
    my_model.train_data(dataframe=dataframe)
    res = my_model.predict_data(dataframe=dataframe)

    return {"model": "LinearRegressor", "data":res}


# @router.get("/agence/year/{year}/mois/{month}/agence/{agence}", name="Get commission filter by year, month and agence")  



