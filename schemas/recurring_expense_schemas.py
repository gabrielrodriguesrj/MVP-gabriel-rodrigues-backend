from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum

class FrequencyEnum(str, Enum):
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"
    yearly = "yearly"

class RecurringExpenseCreateSchema(BaseModel):
    name: str
    description: Optional[str] = None
    amount: float
    frequency: FrequencyEnum
    next_due_date: date
    category: Optional[str] = None
    user_id: int

class RecurringExpenseUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[float] = None
    frequency: Optional[FrequencyEnum] = None
    next_due_date: Optional[date] = None
    category: Optional[str] = None
    is_active: Optional[bool] = None

class RecurringExpenseResponseSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    amount: float
    frequency: str
    next_due_date: Optional[str] = None
    category: Optional[str] = None
    is_active: bool
    user_id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True

