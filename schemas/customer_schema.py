from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class CustomerBase(BaseModel):
    first_name: str        = Field(..., max_length=40)
    last_name: str         = Field(..., max_length=20)
    company: str           = Field(..., max_length=80)
    address: str           = Field(..., max_length=70)
    city: str              = Field(..., max_length=40)
    state: str             = Field(..., max_length=40)
    country: str           = Field(..., max_length=40)
    postal_code: str       = Field(..., max_length=10)
    phone: str             = Field(..., max_length=24)
    fax: Optional[str]     = Field(None, max_length=24)
    email: EmailStr

class EustomerCreate(CustomerBase):
    """
    Inherits all fields from EmployeeBase.
    Used for POST /employees payloads.
    """
    pass

class CustomerUpdate(BaseModel):
    first_name: Optional[str]      = Field(None, max_length=40)
    last_name: Optional[str]       = Field(None, max_length=20)
    company: Optional[str]         = Field(None, max_length=80)
    address: Optional[str]         = Field(None, max_length=70)
    city: Optional[str]            = Field(None, max_length=40)
    state: Optional[str]           = Field(None, max_length=40)
    country: Optional[str]         = Field(None, max_length=40)
    postal_code: Optional[str]     = Field(None, max_length=10)
    phone: Optional[str]           = Field(None, max_length=24)
    fax: Optional[str]             = Field(None, max_length=24)
    email: Optional[EmailStr]      = None

class CustomerRead(CustomerBase):
    employee_id: int

    class Config:
        from_attributes = True
