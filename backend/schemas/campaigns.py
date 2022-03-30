from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from db.models.campaigns import Campaign
  

class CampCreate(BaseModel):
    requestTime : str
    instanceId : str
    xid : str
    partner : str
    recordId : str
    userId : str
    seatId : str
    adunitId : str
    client : str
    event : str
    cid : str
    cname : str
    crid : str
    crtype : str
    crname : str
    sid : str
    sname : str
    ioid : str
    tid : str
    tname : str
    requestId : str
    impressionId : str
    os : str
    browser : str
    country : str
    state : str
    city  : str
    make : str
    model : str
    deviceType : str
    domain : str
    size : str
    winprice : str
    cur : str
    logTime : str
    appflag : str
    dspuid : str
    appBundle : str
    advid : str
    advname : str

class ShowCampaign(BaseModel):
    requestTime : str
    instanceId : str
    xid : str
    partner : str
    recordId : str
    userId : str
    seatId : str
    adunitId : str
    client : str
    event : str
    cid : str
    cname : str
    crid : str
    crtype : str
    crname : str
    sid : str
    sname : str
    ioid : str
    tid : str
    tname : str
    requestId : str
    impressionId : str
    os : str
    browser : str
    country : str
    state : str
    city  : str
    make : str
    model : str
    deviceType : str
    domain : str
    size : str
    winprice : str
    cur : str
    logTime : str
    appflag : str
    dspuid : str
    appBundle : str
    advid : str
    advname : str

    class Config():
        orm_mode=True


