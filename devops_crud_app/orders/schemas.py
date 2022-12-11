from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class OrderSchema(BaseModel):
    name: str
    quantity: int
    total_price: float
    order_datetime: Optional[datetime] = datetime.utcnow()
