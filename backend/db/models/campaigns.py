#users
from enum import unique
from fsspec import Callback
from pytest import Session
from sqlalchemy import  Column, Integer, Float, String, Boolean, ForeignKey, DateTime, insert
from sqlalchemy.orm import relationship
import pandas as pd
import psycopg2
from db.base_class import Base

class Campaign(Base):
    __tablename__ = 'Callback'
    #id = Column(Integer,primary_key= True, index=True)
    
    #campaign_name = Column(String,unique=True, nullable=False)
    requestTime = Column(String, unique=False, nullable=False)
    instanceId = Column(String,unique=False, nullable=False)
    xid = Column(String,unique=False, nullable=False,primary_key= True, index=True)
    partner = Column(String,unique=False, nullable=False)
    recordId = Column(String,unique=False, nullable=False)
    userId = Column(String,unique=False, nullable=True)
    seatId = Column(String,unique=False, nullable=True)
    adunitId = Column(String,unique=False, nullable=False)
    client = Column(String,unique=False, nullable=True)
    event = Column(String,unique=False, nullable=True)
    cid = Column(String, unique=False, nullable=False)
    cname = Column(String, unique=False, nullable=False)
    crid = Column(String,unique=False, nullable=False)
    crtype = Column(String, unique=False, nullable=False)
    crname = Column(String, unique=False, nullable=False)
    sid = Column(String,unique=False, nullable=False)#,primary_key= True, index=True
    sname = Column(String, unique=False, nullable=False)
    ioid = Column(String,unique=False, nullable=False)
    tid = Column(String,unique=False, nullable=False)
    tname = Column(String, unique=False, nullable=False)
    requestId = Column(String, unique=False, nullable=True)
    impressionId = Column(String, unique=False, nullable=False)
    os = Column(String, unique=False, nullable=False)
    browser = Column(String, unique=False, nullable=False)
    country = Column(String, unique=False, nullable=False)
    state = Column(String, unique=False, nullable=False)
    city  = Column(String, unique=False, nullable=False)
    make = Column(String, unique=False, nullable=False)
    model = Column(String, unique=False, nullable=False)
    deviceType = Column(String, unique=False, nullable=False)
    domain = Column(String, unique=False, nullable=False)
    size = Column(String, unique=False, nullable=False)
    winprice = Column(String, unique=False, nullable=False)
    cur = Column(String, unique=False, nullable=False)
    logTime = Column(String, unique=False, nullable=False)
    appflag = Column(String, unique=False, nullable=False)
    dspuid = Column(String, unique=False, nullable=False)
    appBundle = Column(String, unique=False, nullable=False)
    advid = Column(String,unique=False, nullable=False)
    advname = Column(String, unique=False, nullable=False)


    
    #budget_remaining = Column(Float,unique=False, nullable=False)
    #buying_type = Column(String, nullable=False)
    #is_active = Column(Boolean(),default = True)
    #is_superuser = Column(Boolean(),default=False)
    #costs = relationship("Cost",back_populates="owner")



     