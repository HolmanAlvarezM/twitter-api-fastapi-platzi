# Python
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    
class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=3,
        max_length=30
    )
    last_name: str = Field(
        ...,
        min_length=3,
        max_length=30
    )
    birth_date: Optional[date] = Field(default=None)