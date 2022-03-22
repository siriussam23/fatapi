from distutils.version import Version
from fastapi import FastAPI, Request
from core.config import Settings
from db.session import engine
from db.base import Base 
from db.models.costs import cpm
from pydantic import BaseModel
from typing import Optional
from numpy import random

#ran = random.randint(1000,9000)
def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=Settings.PROJECT_TITLE, version=Settings.PROJECT_VERSION)
    create_tables()
    return app

app = start_application()

@app.get("/")
def hello_api():
    ran = random.randint(1000,9000)
    return {"detail":ran}

@app.post("/dummypath")
async def get_body(request: Request):
    return await request.json()

@app.post("/cpm/")
async def create_item(cpm: Request):
    return cpm