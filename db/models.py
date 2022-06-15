from xmlrpc.client import DateTime
from sqlalchemy import Column, Float, Integer, BigInteger, DateTime
from db.database import Base

class Information(Base):

    """
    DB model
    """
    __tablename__ = "info"

    id = Column(Integer, primary_key=True)
    order_id = Column(BigInteger)
    cost_in_dollars = Column(Float)
    cost_in_rubbles = Column(Float)
    delivery_date = Column(DateTime)
    created_date = Column(DateTime)