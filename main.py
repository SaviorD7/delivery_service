from fastapi import FastAPI, BackgroundTasks, Response, Depends, HTTPException, Request
import json
from db.database import SessionLocal, engine
from sqlalchemy.orm import Session
from api.data import router
from db import models


models.Base.metadata.create_all(bind=engine) 

app = FastAPI()



@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(router)

