import uvicorn, os
from fastapi import FastAPI, APIRouter, UploadFile, File

from fastapi.responses import ORJSONResponse, HTMLResponse, JSONResponse, UJSONResponse

from models.LinearRegressor import LinearRegressorModel
from models.LogisticRegressor import LogisticRegressorModel

from pathlib import Path
import shutil # save upload file
import uuid

import pandas as pd, pandas


regressor_router = APIRouter() # FastAPI()



# home
url1 = "https://raw.githubusercontent.com/datagy/data/main/insurance.csv" # x=charges y=age
url2 = "https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/difficile.csv" # x=libido y=dose
@regressor_router.post("/processing", tags=["regressor"])   
async def home(filepath:str, features:str="dose", label:str="libido"):
    """
    > **features:str**
    >> Variables à predire (ex: y)
    ---
    > **label:str**
    >> Variables explicatives(ex: var1,var2,...)
    """

    # Creating two arrays for the feature and target
    features = features.split(",")
    label = label

    result = {}

    for model in [LinearRegressorModel(), LogisticRegressorModel()]:

        # model = LogisticRegressorModel()
        model_name = model.model_name

        df = model.read_data(url=filepath)

        X = df[features].astype(int)
        y = df[label].astype(int)

        dataframe = model.split_data(features=X, label=y)
        model.train_data(dataframe=dataframe)

        pred = model.predict_data(dataframe=dataframe)
        
        y_test = dataframe[-1]
        evaluate = model.evaluate_data(y_test=y_test, predictions=pred)
        
        result[model_name] = evaluate

        print('---------')

    return result


