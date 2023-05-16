# Python
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import BaseModel, EmailStr, Field

class userBase(BaseModel):
    user_id = UUID = Field(...)
    email = EmailStr = Field(...)
    
class userLogin(userBase):
    password = str = Field(
        ...,
        min_length=8
    )

class user(userBase):
    first_name = str = Field(
        ...,
        min_length=3,
        max_length=30
    )
    last_name = str = Field(
        ...,
        min_length=3,
        max_length=30
    )
    birth_date = Optional[date] = Field(default=None)