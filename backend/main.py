#from distutils.version import Version
#from xml.etree.ElementInclude import include
from fastapi import FastAPI, Request
from core.config import Settings
from db.session import engine
from db.base import Base 
from apis.base import api_router
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
 

from numpy import random

#ran = random.randint(1000,9000)
def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(title=Settings.PROJECT_TITLE, version=Settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app

app = start_application()

@app.get("/")
def hello_api():
    df = pd.read_json('/Users/santosh/Downloads/Data_1/callback/bidderCallbackUpdate_2022-03-09_00.log',lines=True)
    num_row = len(df.loc[:,"winprice"])
    cpm =[]
    for w in range(num_row-15,num_row):
        cpm.append(df.loc[w,"winprice"])
    a=np.array(cpm)
    b=np. mean(a)
    c=("%.2f" %b)

    return {"detail":c}


