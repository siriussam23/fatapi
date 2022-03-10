from sqlalchemy import  Column, Integer, Float, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

class cpm(Base):
    __tablename__ = 'Cost'
    id = Column(Integer,primary_key= True, index=True)
    total_cost = Column(Float, nullable=False)
    total_recipients = Column(Float, nullable=False)
    date_posted = Column(DateTime)
    is_active = Column(Boolean(),default = True)
    owner_id = Column (Integer, ForeignKey('accounts.id'))
    owner = relationship("Campaign", back_populates= "costs")



