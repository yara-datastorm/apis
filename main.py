import uvicorn, os, logging
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from mlearning import regressor_router
from commons import common_router

from core.logger import get_logger

app = FastAPI(
    title="YARA-DataStorm",
    description="""**ML APP**""",
    version="0.0.1",
    contact={
        "name": "Armel DREY",
        "email": "armeldrey@gmail.com",
    },
)


#in any file that import fn get_logger, you can set up local logger like:
# logger = get_logger()
# logger = get_logger(__name__)



origins = [
    "http://localhost",
    "http://localhost:3001",
    "http://test.localhost:3001",
    "http://localhost:3000",
    "http://test.localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(linear_regressor_router, tags=["RegressorLinear"], prefix="/linear_regressor")
# app.include_router(logistic_regressor_router,tags=["Regressorlogistic"], prefix="/logistic_regressor")
# app.include_router(vendeur_router,tags=["vendeur"], prefix="/ventesim")


APP_PORT = os.environ.get("APP_PORT", default=8080)
APP_RELOAD = os.environ.get("APP_RELOAD", default=False)
APP_WORKERS = os.environ.get("APP_WORKERS", default=1)




# app.mount("/models", regressor_router)
# app.mount("/subapi2", regressor_router)
# app.include_router(regressor_router)

app.include_router(regressor_router, prefix="/regressor")
app.include_router(common_router, prefix="/common")


# http://test.localhost:8017/subapi/docs#/



@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    logger.info("doc page")
    return RedirectResponse(url='/docs')



if __name__ == "__main__":
    logger.info("Yara started..")

    uvicorn.run("main:app", host="0.0.0.0", port=int(APP_PORT), reload=APP_RELOAD, workers=int(APP_WORKERS))



