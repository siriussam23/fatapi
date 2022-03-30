from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.campaigns import CampCreate, ShowCampaign
from db.session import get_db
from db.repository.campaigns import create_new_campaign, callback_db

router = APIRouter()


@router.post("/",response_model=ShowCampaign) #@router.post("/") apis/base.py we have used
def create_campaign(campaign:CampCreate, db:Session=Depends(get_db)):
    campaign = callback_db(campaign, db)
    #campaign = create_new_campaign(campaign, db)
    return campaign

    #class Config():
    #    orm_mode=True
