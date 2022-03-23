#users
from sqlalchemy import  Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Campaign(Base):
    __tablename__ = 'Campaign'
    id = Column(Integer,primary_key= True, index=True)
    campaign_name = Column(String,unique=True, nullable=False)
    budget_remaining = Column(Float,unique=False, nullable=False)
    buying_type = Column(String, nullable=False)
    is_active = Column(Boolean(),default = True)
    is_superuser = Column(Boolean(),default=False)
    costs = relationship("cpm",back_populates="owner")
     
