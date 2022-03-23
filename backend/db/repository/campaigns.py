from sqlalchemy.orm import Session

from schemas.campaigns import CampCreate
from db.models.campaigns import Campaign


def create_new_campaign(campaign: CampCreate,db: Session):
    campaign = Campaign(campaign_name=campaign.campaign_name,
    budget_remaining=campaign.budget_remaining,
    buying_type=campaign.buying_type,
    is_active=True,
    is_superuser=False
    )

    db.add(campaign)
    db.commit()
    db.refresh(campaign)
    return campaign




