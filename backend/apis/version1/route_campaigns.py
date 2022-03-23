from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.campaigns import CampCreate
from db. session import get_db
from db.repository.campaigns import create_new_campaign

router = APIRouter()


@router.post("/") #@router.post("/campaign") apis/base.py we have used
def create_campaign(campaign:CampCreate, db:Session=Depends(get_db)):
    campaign = create_new_campaign(campaign, db)
    return campaign
