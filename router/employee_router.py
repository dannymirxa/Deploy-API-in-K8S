from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession
from database import database
from models.employee_model import Employee
from schemas.employee_schema import (
    EmployeeCreate,
    EmployeeRead,
    EmployeeUpdate,
    EmployeeTotalSales,
    EmployeePerformanceRequest,
    EmployeePerformanceRead
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

@router.get("/total_sales", response_model=list[EmployeeTotalSales])
async def get_employee_total_sales(db: AsyncSession = Depends(database.get_session)):
    """
    Returns a list of employees with their total sales, ordered by total sales descending.
    """
    async with db as session:
        stmt = text("""
            SELECT e.first_name, e.last_name, SUM(i.Total) AS TotalSales
            FROM employee AS e
            JOIN customer AS c ON e.employee_id = c.support_rep_id
            JOIN invoice AS i ON c.customer_id = i.customer_id
            GROUP BY e.first_name, e.last_name
            ORDER BY TotalSales DESC
        """)
        result = await session.execute(stmt)
        rows = result.mappings().all()
        return [EmployeeTotalSales(**row) for row in rows]

@router.post("/employee_performance", response_model=list[EmployeePerformanceRead])
async def get_employee_total_sales(employee_performance_request: EmployeePerformanceRequest, db: AsyncSession = Depends(database.get_session)):
    """
    Returns a list of employees with their total sales, ordered by total sales descending.
    """
    async with db as session:
        stmt = text("""
            SELECT 
                e.employee_id,
                e.first_name ,
                e.last_name,
                e.title,
                COUNT(DISTINCT c.customer_id) AS CustomersHandled,
                SUM(i.total) AS totalSales,
                ROUND(AVG(i.total), 2) AS AvgInvoiceValue
            FROM employee e
            JOIN customer c 
                ON e.employee_id = c.support_rep_id
            JOIN invoice i 
                ON c.customer_id = i.customer_id
            WHERE e.title LIKE :title
            AND i.invoice_date >= :invoice_date
            GROUP BY e.employee_id, e.first_name, e.last_name, e.title
            HAVING SUM(i.total) > 50 
            ORDER BY totalSales DESC;
        """)
        result = await session.execute(stmt, {"title": f'%{employee_performance_request.title}%', "invoice_date": employee_performance_request.invoice_date})
        rows = result.mappings().all()
        return [EmployeePerformanceRead(**row) for row in rows]

@router.get("/employee/{employee_id}", response_model=EmployeeRead)
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
