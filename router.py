from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from typing import List
import psycopg2.extras 
import json
from psycopg2 import Error
from schemas import EmployeeHighestSalesGet, AristwithAlbumbyGenrePost
from database import get_db_connection

router = APIRouter()

@router.get("/EmployeeHighestSalesGet/")
async def get_EmployeeHighestSales():
    query = text("""SeLeCT e.first_name , e.last_name , SUM(i.Total) AS TotalSales 
                    FROM employee AS e 
                        JOIN customer AS c ON e.employee_id  = c.support_rep_id  
                        JOIN invoice AS i ON c.customer_id  = i.customer_id  
                    GROUP BY e.first_name , e.last_name  ORDeR BY TotalSales DeSC""")
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(query)
    results = cur.fetchall()

    if not results:
        raise HTTPException(status_code=404, detail='Employee does not exist')
    conn.close()

    employees = json.dumps(results, default=str)
    # print(type(json.loads(employees)))
    return json.loads(employees)