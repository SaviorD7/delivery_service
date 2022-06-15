from genericpath import exists
from locale import normalize
from typing import List
import logging
from venv import create
import requests
from fastapi import APIRouter, HTTPException, UploadFile, File, Request, BackgroundTasks, Response, Depends
from db.database import SessionLocal, engine
from sqlalchemy.orm import Session
import datetime as dt

from db import crud, schemas
from utils.data import get_data_from_sheet
from utils.helper import convert_data

router = APIRouter()

# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", level=logging.INFO)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.get('/upload_data')
async def upload_data(response: Response, db: Session = Depends(get_db)):

    """
    Upload data from GS
    """

    response.headers["Access-Control-Allow-Origin"] = "*"
    try:
        data = get_data_from_sheet()
        normalize_data = convert_data(data)
        for pack in normalize_data:
            crud.add_info(db=db,
            exp=schemas.Information(id=pack[0],
            order_id=pack[1],
            cost_in_dollars=pack[2],
            cost_in_rubbles=pack[3],
            delivery_date=pack[4],
            created_date = dt.datetime.now()))
    except Exception as e:
        return {"result": 'Error: {}'.format(e) }
    return {"result": "Done"}


@router.get('/update_data')
async def update_data(response: Response, db: Session = Depends(get_db)):
    """
    Update data from GS.
    Delete row from table if id does not exist anymore in GS
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    try:
        data = get_data_from_sheet()
        normalize_data = convert_data(data)
        exists_id = crud.get_all_id(db)
        print(normalize_data)
        for pack in normalize_data:
            if pack[0] in exists_id:
                exists_id.remove(pack[0])
                crud.update_info(db=db,
                id=pack[0],
                order_id=pack[1],
                cost_in_dollars=pack[2],
                cost_in_rubbles=pack[3],
                delivery_date=pack[4])
        for ids in exists_id:
            crud.delete_by_id(db, ids)
    except Exception as e:
        return {"result": 'Error: {}'.format(e) }
    return {"result": "Done"}



    