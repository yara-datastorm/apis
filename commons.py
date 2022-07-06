import uvicorn, os
from fastapi import FastAPI, APIRouter, UploadFile, File, HTTPException

from fastapi.responses import ORJSONResponse, HTMLResponse, JSONResponse, UJSONResponse

from models.LinearRegressor import LinearRegressorModel
from models.LogisticRegressor import LogisticRegressorModel

from pathlib import Path
import shutil # save upload file
import uuid

import pandas as pd, pandas


common_router = APIRouter() # FastAPI()


def chunksize_data(data_url,sep,chuncksize=1000):
    # chuncksize
    chunks = pd.read_csv(filepath_or_buffer=data_url, sep=sep, chunksize=chuncksize)  # the number of rows per chunk

    df = []
    for dframe in chunks:
        df.append(dframe)

    df = pd.concat(df,sort=False)
    return df

def memory_data(file_path, limit=10000000):
    # limit 10Mb
    file_size = os.path.getsize(file_path)
    unit = 'Bytes'

    if file_size > limit: 
        return None, {'msg': 'error: max file size is 10Mb'}
    
    if file_size < 10**6:
        unit = 'Bytes'
        filesize = file_size
    elif file_size < 10**9:
        unit = 'Kb'
        filesize = file_size*10**-3
    elif file_size < 10**12:
        nit = 'Mb'
        filesize = file_size*10**-6
    elif file_size < 10**15:
        unit = 'Gb'
        filesize = file_size*10**-9
    else:
        unit = 'Tb'
        filesize = file_size*10**-12
        
    return {'memory': f'{filesize}', 'unit': f'{unit}'}, None
    


@common_router.post("/upload_file", tags=["upload"])   
async def upload_file(file:UploadFile=File(...)):
    """
    > **file:str**
    >> Variables à predire (ex: y)
    """
    try:
        myuuid = uuid.uuid4()
        fname = "{}#{}".format(myuuid, file.filename)
        file_path = "static/{}".format(fname)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))

    return {"old_filename": file.filename, "filename": fname, "filepath": file_path}

@common_router.post("/read_url", tags=["upload"])  
async def read_url(data_url:str, sep:str=','):
    """
    > **file:str**
    >> Variables à predire (ex: y)
    """

    if data_url.endswith('.csv'):
        df = chunksize_data(data_url=data_url,sep=sep)
        
        print()
        
        myuuid = uuid.uuid4()
        fname = "{}#{}".format(myuuid, data_url.split('/')[-1])
        file_path = "static/{}".format(fname)

        df.to_csv(file_path, sep=sep, index=False)

        memory, _ = memory_data(file_path)
        if _ != None:
            raise HTTPException(status_code=404, detail=_)
        

        return {"url": data_url, "filename": fname, "filepath": file_path}

    else:
        pass

    return False


@common_router.get("/dataframe/columns", tags=["info"])   
async def data_info_columns(filepath:str, sep:str=','):
    """
    > **features:str**
    >> Variables à predire (ex: y)
    """
    print("info columns...")
    df = pd.read_csv(filepath, sep=sep)
    return {'columns': list(df.columns)}

@common_router.get("/dataframe/columns_type", tags=["info"])   
async def data_info(filepath:str, sep:str=','):
    """
    > **features:str**
    >> Variables à predire (ex: y)
    """
    print("info columns...")
    df = pd.read_csv(filepath, sep=sep)
    df = pd.DataFrame(df.dtypes, columns=["type"])
    
    
    df['type'] = df['type'].apply(str)
    df = df.reset_index()

    df.rename({'index':'column'}, axis=1, inplace=True)
    
    res = df.to_dict('records')
    print(res)

    # static/f0369d5d-1c22-4599-84a1-79e0dfb63fae#credit_data.csv
    print('##')

    return list(res)

@common_router.get("/dataframe/shape", tags=["info"])   
async def data_info_shape(filepath:str, sep:str=','):
    """
    > **features:str**
    >> Variables à predire (ex: y)
    """
    print("info shape...")
    df = pd.read_csv(filepath, sep=sep)
    print(df.shape)
    return {'dim': str(df.shape)}




