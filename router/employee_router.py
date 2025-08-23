from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession
from database import database
from models.employee_model import Employee
from schemas.employee_schema import (
    EmployeeCreate,
    EmployeeRead,
    EmployeeUpdate,
)
router = APIRouter(prefix="/employees")

@router.get("/", response_model=list[EmployeeRead])
async def get_all_emloyee(db: AsyncSession = Depends(database.get_session)):
    """
    The db object, which is the result of Depends(database.get_session), is an asynchronous context manager. To access the AsyncSession object and its execute method, it needs to be entered using async with
    """
    async with db as session:
        result = await session.execute(select(Employee))
        employee = result.scalars().all()
        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee does not exist"
            )
        return employee

@router.get("/{employee_id}", response_model=EmployeeRead)
async def get_employee_by_id(employee_id: int, db: AsyncSession = Depends(database.get_session)):
    async with db as session:
        result = await session.execute(
            select(Employee)
            .where(Employee.employee_id == employee_id)
        )
        employee = result.scalars().first()
        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee with id={employee_id} not found"
            )
        return employee