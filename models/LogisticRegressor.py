from fastapi import APIRouter, HTTPException
import os

router = APIRouter()


# home
@router.get("/")   
async def home():
    return {"msg": "LogisticRegressor"}


# @router.get("/agence/year/{year}/mois/{month}/agence/{agence}", name="Get commission filter by year, month and agence")  