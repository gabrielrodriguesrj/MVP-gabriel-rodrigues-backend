from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr

class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None

class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: str
    created_at: Optional[str] = None

    class Config:
        from_attributes = True

