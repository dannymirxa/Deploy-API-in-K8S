from main import app
import pytest
import httpx
import pytest_asyncio

@pytest_asyncio.fixture
async def client():
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        yield client

@pytest.mark.asyncio
async def test_get_employee(client):
    response = await client.get("/employees/")
    assert response.status_code == 200
    assert set(response.json()[0].keys()) == {'title', 'birth_date', 'phone', 'postal_code', 'hire_date', 'country', 'city', 'first_name', 'last_name', 'address', 'fax', 'email', 'employee_id', 'reports_to', 'state'}

@pytest.mark.asyncio
async def test_get_employee_total_sales(client):
    response = await client.get("/employees/total_sales")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert set(response.json()[0].keys()) == {'first_name', 'last_name', 'totalsales'}

@pytest.mark.asyncio
async def test_get_employee_by_id(client):
    # Assuming employee with ID 1 exists
    response = await client.get("/employees/employee/1")
    assert response.status_code == 200
    employee_data = response.json()
    assert employee_data['employee_id'] == 1
    assert set(employee_data.keys()) == {'title', 'birth_date', 'phone', 'postal_code', 'hire_date', 'country', 'city', 'first_name', 'last_name', 'address', 'fax', 'email', 'employee_id', 'reports_to', 'state'}

    # Test for non-existent employee
    response = await client.get("/employees/employee/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Employee with id=999 not found"}

@pytest.mark.asyncio
async def test_get_employee_performance(client):
    request_payload = {
        "title": "Sales Support Agent",
        "invoice_date": "2009-01-01"
    }
    response = await client.post("/employees/employee_performance", json=request_payload)
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert set(response.json()[0].keys()) == {'employee_id', 'first_name', 'last_name', 'customershandled', 'totalsales', 'avginvoicevalue'}
    request_payload_no_match = {
        "title": "NonExistentTitle",
        "invoice_date": "2009-01-01"
    }
    response_no_match = await client.post("/employees/employee_performance", json=request_payload_no_match)
    assert response_no_match.status_code == 200
    assert response_no_match.json() == []