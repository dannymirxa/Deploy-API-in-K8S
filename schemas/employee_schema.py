"""
Which employee has the highest total sales amount (invoice total) to customers they support? The final result should show the employee's full name and their total sales.

SeLeCT e.first_name , e.last_name , SUM(i.Total) AS TotalSales 
	FROM employee AS e 
		JOIN customer AS c ON e.employee_id  = c.support_rep_id  
		JOIN invoice AS i ON c.customer_id  = i.customer_id  
	GROUP BY e.first_name , e.last_name  ORDeR BY TotalSales DeSC
"""

"""Which artists have albums that include tracks with the genre 'Rock'? The query should return a unique list of artist names.

SELECT DISTINCT Ar."name"  FROM artist AS Ar 
	JOIN album AS Al ON Ar.artist_id  = Al.artist_id 
	JOIN track AS T ON Al.album_id  = T.album_id 
	JOIN genre AS G ON T.genre_id  = G.genre_id 
		WHERE G."name" = 'Rock' ORDER BY Ar."name" ;
"""
# app/schemas/employee_schema.py

from datetime import datetime, date
from typing import Optional
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class EmployeeBase(BaseModel):
    first_name: str        = Field(..., max_length=20)
    last_name: str         = Field(..., max_length=20)
    title: str             = Field(..., max_length=30)
    reports_to: Optional[int] = None
    birth_date: datetime
    hire_date: datetime
    address: str           = Field(..., max_length=70)
    city: str              = Field(..., max_length=40)
    state: str             = Field(..., max_length=40)
    country: str           = Field(..., max_length=40)
    postal_code: str       = Field(..., max_length=10)
    phone: str             = Field(..., max_length=24)
    fax: Optional[str]     = Field(None, max_length=24)
    email: EmailStr

class EmployeeCreate(EmployeeBase):
    """
    Inherits all fields from EmployeeBase.
    Used for POST /employees payloads.
    """
    pass

class EmployeeUpdate(BaseModel):
    first_name: Optional[str]      = Field(None, max_length=20)
    last_name: Optional[str]       = Field(None, max_length=20)
    title: Optional[str]           = Field(None, max_length=30)
    reports_to: Optional[int]      = None
    birth_date: Optional[datetime] = None
    hire_date: Optional[datetime]  = None
    address: Optional[str]         = Field(None, max_length=70)
    city: Optional[str]            = Field(None, max_length=40)
    state: Optional[str]           = Field(None, max_length=40)
    country: Optional[str]         = Field(None, max_length=40)
    postal_code: Optional[str]     = Field(None, max_length=10)
    phone: Optional[str]           = Field(None, max_length=24)
    fax: Optional[str]             = Field(None, max_length=24)
    email: Optional[EmailStr]      = None

class EmployeeRead(EmployeeBase):
    employee_id: int

    class Config:
        from_attributes = True

class EmployeeTotalSales(BaseModel):
    first_name: str = Field(None, max_length=20)
    last_name: str = Field(None, max_length=20)
    totalsales: Decimal = None

    # class Config:
    #     from_attributes = True

class EmployeePerformanceRequest(BaseModel):
    title: Optional[str]
    invoice_date: Optional[date]

class EmployeePerformanceRead(BaseModel):
    employee_id: int
    first_name: str = Field(None, max_length=50)
    last_name: str = Field(None, max_length=50)
    customershandled: int
    totalsales: Decimal = None
    avginvoicevalue: Decimal = None
