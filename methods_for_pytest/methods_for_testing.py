from main import app
import pytest
import httpx
import asyncio


async def create_client():
    return httpx.AsyncClient(base_url="http://localhost:8000")

async def get_employee_total_sales():
    client_instance = await create_client()
    try:
        response = await client_instance.get("/employees/total_sales")
        assert response.status_code == 200
        assert len(response.json()) > 0
        print(set(response.json()[0].keys()))
    finally:
        await client_instance.aclose()

# Run the get_employee_total_sales coroutine

# asyncio.run(get_employee_total_sales())

async def get_employee_performance():
    client_instance = await create_client()
    request_payload = {
        "title": "Sales Support Agent",
        "invoice_date": "2009-01-01"
    }
    response = await client_instance.post("/employees/employee_performance", json=request_payload)
    assert response.status_code == 200
    assert len(response.json()) > 0
    print(response.json()[0].keys())
    assert set(response.json()[0].keys()) == {'employee_id', 'first_name', 'last_name', 'customershandled', 'totalsales', 'avginvoicevalue'}
asyncio.run(get_employee_performance())
