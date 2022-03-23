from pickletools import float8
from typing import Optional
from pydantic import BaseModel

from db.models.campaigns import Campaign
  

class CampCreate(BaseModel):
    campaign_name : str    
    budget_remaining : float
    buying_type : str
