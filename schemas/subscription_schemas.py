from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum

class BillingCycleEnum(str, Enum):
    monthly = "monthly"
    yearly = "yearly"
    weekly = "weekly"

class SubscriptionCreateSchema(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    billing_cycle: BillingCycleEnum
    next_billing_date: date
    category: Optional[str] = None
    user_id: int

class SubscriptionUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    billing_cycle: Optional[BillingCycleEnum] = None
    next_billing_date: Optional[date] = None
    category: Optional[str] = None
    is_active: Optional[bool] = None

class SubscriptionResponseSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    billing_cycle: str
    next_billing_date: Optional[str] = None
    category: Optional[str] = None
    is_active: bool
    user_id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True

