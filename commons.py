import uvicorn, os
from fastapi import FastAPI, APIRouter, UploadFile, File, HTTPException

from fastapi.responses import ORJSONResponse, HTMLResponse, JSONResponse, UJSONResponse

from models.LinearRegressor import LinearRegressorModel
from models.LogisticRegressor import LogisticRegressorModel

from pathlib import Path
import shutil # save upload file
import uuid

import pandas as pd
from pydantic import BaseModel

from core import chunksize_data, memory_data, validate_url

# import logger 
from core.logger import *


common_router = APIRouter() # FastAPI()

class UploadWithUrlInputModel(BaseModel):
    data_url:str
    sep:str = ","

class InfoColumnsInputModel(BaseModel):
    filepath:str
    sep:str = ","


@common_router.post("/upload_file", tags=["upload"])   
async def upload_file(file:UploadFile=File(...)):
    """
    > **file:str**
    >> Variables à predire (ex: y)
    """
    try:
        myuuid = uuid.uuid4()
        fname = "{}#{}".format(myuuid, file.filename)
        fname = fname.split(' ')
        fname = ''.join(fname)

        file_path = "static/{}".format(fname)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as ex:
        logger.error(f'upload file {ex}')
        raise HTTPException(status_code=404, detail=str(ex))

    res = {"old_filename": file.filename, "filename": fname, "filepath": file_path}
    logger.info(f'upload file {res}')
    return res

@common_router.post("/read_url", tags=["upload"])  
async def read_url(data:UploadWithUrlInputModel):
    """
    > **file:str**
    >> Variables à predire (ex: y)
    """
    try:
        data_url = data.data_url
        sep = data.sep

        if validate_url(data_url): # if data_url is link
            if data_url.endswith('.csv'):
                df = chunksize_data(data_url=data_url,sep=sep)
                
                myuuid = uuid.uuid4()
                fname = "{}#{}".format(myuuid, data_url.split('/')[-1])
                file_path = "static/{}".format(fname)

                df.to_csv(file_path, sep=sep, index=False)

                memory, _ = memory_data(file_path)
                if _ != None:
                    raise HTTPException(status_code=404, detail=_)
            
                res = {"url": data_url, "filename": fname, "filepath": file_path}
                logger.info(f'read url {res}')
                return res
            else:
                logger.info(f'read url : file is not csv')
                pass
        else:
            logger.error(f'{data_url} is not link')
            raise HTTPException(status_code=404, detail=f"{data_url} is not link") 
    except Exception as ex:
        logger.error(f'read url {ex}')
        raise HTTPException(status_code=404, detail=str(ex))

    raise HTTPException(status_code=404, detail=str('read url  error'))


@common_router.post("/dataframe/columns", tags=["info"])   
async def data_info_columns(data:InfoColumnsInputModel):
    """
    > **features:str**
    >> Variables à predire (ex: y)
    """
    try:
        filepath = data.filepath
        sep = data.sep

        print("info columns...")
        df = pd.read_csv(filepath, sep=sep)

        res = {'columns': list(df.columns)}
        logger.info(f'data info columns {res}')
        return res
    except Exception as ex:
        logger.error(f'data info columns {ex}')
        raise HTTPException(status_code=404, detail=str(ex))

@common_router.post("/dataframe/columns_type", tags=["info"])   
async def data_info_columns_type(filepath:str, sep:str=','):
    """
    > **features:str**
    >> Variables à predire (ex: y)
    """
    try:
        df = pd.read_csv(filepath, sep=sep)
        df = pd.DataFrame(df.dtypes, columns=["type"])
        
        df['type'] = df['type'].apply(str)
        df = df.reset_index()

        df.rename({'index':'column'}, axis=1, inplace=True)
        res = df.to_dict('records')

        # static/f0369d5d-1c22-4599-84a1-79e0dfb63fae#credit_data.csv

        res = list(res)
        logger.info(f'data info columns {res}')
        return res

    except Exception as ex:
        logger.error(f'data info columns {res}')
        raise HTTPException(status_code=404, detail=str(ex))

@common_router.get("/dataframe/shape", tags=["info"])   
async def data_info_shape(filepath:str, sep:str=','):
    """
    > **features:str**
    >> Variables à predire (ex: y)
    """
    try:
        df = pd.read_csv(filepath, sep=sep)
        res = {'dim': str(df.shape)}
        logger.info(f'data info columns {res}')
        return res
    except Exception as ex:
        logger.error(f'data info columns {res}')
        raise HTTPException(status_code=404, detail=str(ex))




