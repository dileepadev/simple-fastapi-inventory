from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
