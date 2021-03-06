import uvicorn, os
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware


from mlearning import regressor_router
from commons import common_router


app = FastAPI(
    title="YARA-DataStorm",
    description="""**ML APP**""",
    version="0.0.1",
    contact={
        "name": "Armel DREY",
        "email": "armeldrey@gmail.com",
    },
)


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



if __name__ == "__main__":
    print("Yara started..")

    uvicorn.run("main:app", host="0.0.0.0", port=int(APP_PORT), reload=APP_RELOAD, workers=int(APP_WORKERS))



