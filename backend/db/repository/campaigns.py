from sqlalchemy.orm import Session

from schemas.campaigns import CampCreate
from db.models.campaigns import Campaign
import pandas as pd
import psycopg2


def create_new_campaign(campaign: CampCreate,db: Session):
    campaign = Campaign(requestTime=campaign.requestTime,
    instanceId=campaign.instanceId,
    xid=campaign.xid,
    partner=campaign.partner,
    recordId=campaign.recordId,
    userId=campaign.userId,
    seatId=campaign.seatId,
    adunitId=campaign.adunitId,
    client=campaign.client,
    event=campaign.event,
    cid=campaign.cid,
    cname=campaign.cname,
    crid=campaign.crid,
    crtype=campaign.crtype,
    crname=campaign.crname,
    sid=campaign.sid,
    sname=campaign.sname,
    ioid=campaign.ioid,
    tid=campaign.tid,
    tname=campaign.tname,
    requestId=campaign.requestId,
    impressionId=campaign.impressionId,
    os=campaign.os,
    browser=campaign.browser,
    country=campaign.country,
    state=campaign.state,
    city=campaign.city,
    make=campaign.make,
    model=campaign.model,
    deviceType=campaign.deviceType,
    domain=campaign.domain,
    size=campaign.size,
    winprice=campaign.winprice,
    cur=campaign.cur,
    logTime=campaign.logTime,
    appflag=campaign.appflag,
    dspuid=campaign.dspuid,
    appBundle=campaign.appBundle,
    advid=campaign.advid,
    advname=campaign.advname,

    #is_active=True,
    #is_superuser=False
    )

    db.add(campaign)
    db.commit()
    db.refresh(campaign)
    return campaign

def callback_db(campaign: CampCreate,db: Session):
    data = pd.read_json('/Users/santosh/Downloads/Data_1/callback/bidderCallbackUpdate_2022-03-09_00.log',lines=True)
    #cpm = data.loc[:,"winprice"]
    num_row = len(data.loc[:,"winprice"])
    
    for ii in range(0,num_row):
        requestTime1 = data.loc[ii,"requestTime"]
        instanceId1 = data.loc[ii,"instanceId"]
        xid1 = data.loc[ii,"xid"]
        partner1 = data.loc[ii,"partner"]
        recordId1 = data.loc[ii,"recordId"]
        userId1 = data.loc[ii,"userId"]
        seatId1 = data.loc[ii,"seatId"]
        adunitId1 = data.loc[ii,"adunitId"]
        client1 = data.loc[ii,"client"]
        event1 = data.loc[ii,"event"]
        cid1 = data.loc[ii,"cid"]
        cname1= data.loc[ii,"cname"]
        crid1 = data.loc[ii,"crid"]
        crtype1 = data.loc[ii,"crtype"]
        crname1 = data.loc[ii,"crname"]
        sid1 = data.loc[ii,"sid"]
        sname1 = data.loc[ii,"sname"]
        ioid1 = data.loc[ii,"ioid"]
        tid1 = data.loc[ii,"tid"]
        tname1 = data.loc[ii,"tname"]
        requestId1 = data.loc[ii,"requestId"]
        impressionId1 = data.loc[ii,"impressionId"]
        os1 = data.loc[ii,"os"]
        browser1 = data.loc[ii,"browser"]
        country1 = data.loc[ii,"country"]
        state1 = data.loc[ii,"state"]
        city1 = data.loc[ii,"city"]
        make1 = data.loc[ii,"make"]
        model1 = data.loc[ii,"model"]
        deviceType1 = data.loc[ii,"deviceType"]
        domain1 = data.loc[ii,"domain"]
        size1 = data.loc[ii,"size"]
        winprice1 = data.loc[ii,"winprice"]
        cur1 = data.loc[ii,"cur"]
        logTime1 = data.loc[ii,"logTime"]
        appflag1 = data.loc[ii,"appflag"]
        dspuid1 = data.loc[ii,"dspuid"]
        appBundle1 = data.loc[ii,"appBundle"]
        advid1 = data.loc[ii,"advid"]
        advname1 = data.loc[ii,"advname"]


        campaign = Campaign(requestTime=str(requestTime1),
        instanceId=str(instanceId1),
        xid=str(xid1),
        partner=str(partner1),
        recordId=str(recordId1),
        userId=str(userId1),
        seatId=str(seatId1),
        adunitId=str(adunitId1),
        client=str(client1),
        event=str(event1),
        cid=str(cid1),
        cname=str(cname1),
        crid=str(crid1),
        crtype=str(crtype1),
        crname=str(crname1),
        sid=str(sid1),
        sname=str(sname1),
        ioid=str(ioid1),
        tid=str(tid1),
        tname=str(tname1),
        requestId=str(requestId1),
        impressionId=str(impressionId1),
        os=str(os1),
        browser=str(browser1),
        country=str(country1),
        state=str(state1),
        city=str(city1),
        make=str(make1),
        model=str(model1),
        deviceType=str(deviceType1),
        domain=str(domain1),
        size=str(size1),
        winprice=str(winprice1),
        cur=str(cur1),
        logTime=str(logTime1),
        appflag=str(appflag1),
        dspuid=str(dspuid1),
        appBundle=str(appBundle1),
        advid=str(advid1),
        advname=str(advname1)

        #is_active=True,
        #is_superuser=False
        )
        db.add(campaign)
        db.commit()
        db.refresh(campaign)

    return campaign




