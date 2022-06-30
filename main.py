import uvicorn, os
from fastapi import FastAPI

from models.LinearRegressor import router as linear_regressor_router
from models.LogisticRegressor import router as logistic_regressor_router
# from vendeur.main import router as vendeur_router


app = FastAPI(
    title="YARA",
    description="""**Linear Regressor**""",
    version="0.0.1",
    contact={
        "name": "Armel DREY",
        "email": "armeldrey@gmail.com",
    },
)
app.include_router(linear_regressor_router, tags=["RegressorLinear"], prefix="/linear_regressor")
app.include_router(logistic_regressor_router,tags=["Regressorlogistic"], prefix="/logistic_regressor")
# app.include_router(vendeur_router,tags=["vendeur"], prefix="/ventesim")


APP_PORT = os.environ.get("APP_PORT", default=8080)
APP_RELOAD = os.environ.get("APP_RELOAD", default=False)
APP_WORKERS = os.environ.get("APP_WORKERS", default=1)


# subapi = FastAPI()
# @subapi.get("/sub")
# def read_sub():
#     return {"message": "Hello World from sub API"}
# app.mount("/subapi", subapi)

# http://test.localhost:8017/subapi/docs#/



if __name__ == "__main__":
    print("Yara started..")

    uvicorn.run("main:app", host="0.0.0.0", port=int(APP_PORT), reload=APP_RELOAD, workers=int(APP_WORKERS))



