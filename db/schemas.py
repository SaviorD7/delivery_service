from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Information(BaseModel):
    """
    Schema of GS data
    """
    id: int
    order_id: int 
    cost_in_dollars: float
    cost_in_rubbles: float
    delivery_date: datetime
    created_date: Optional[datetime]
    class Config:
        orm_mode = True 