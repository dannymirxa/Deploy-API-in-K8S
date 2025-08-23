from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import base

class Customer(base):
    __tablename__ = "customer"
    
    customer_id = Column(Integer, primary_key=True, index=True)
    first_name  = Column(String(40), nullable=False, index=True)
    last_name   = Column(String(20), nullable=False, index=True)
    address     = Column(String(70), nullable=False)
    city        = Column(String(40), nullable=False)
    state       = Column(String(40), nullable=False)
    country     = Column(String(40), nullable=False)
    postal_code = Column(String(10), nullable=False)
    phone       = Column(String(24), nullable=False)
    fax         = Column(String(24), nullable=True)
    email       = Column(String(60), nullable=False, unique=True, index=True)
    support_rep_id = Column(Integer, ForeignKey("employee.employee_id"), nullable=True, index=True)