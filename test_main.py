from main import app
from schemas.employee_schema import (
    EmployeeCreate,
    EmployeeRead,
    EmployeeUpdate,
    EmployeeTotalSales,
    EmployeePerformanceRequest,
    EmployeePerformanceRead
)
import pytest
from fastapi.testclient import TestClient

client = TestClient(app)

@pytest.fixture
def test_get_employee():
    response = client.get("/employees/")
    assert response.status_code == 200
    assert set(response.json()[0].keys()) == {'title', 'birth_date', 'phone', 'postal_code', 'hire_date', 'country', 'city', 'first_name', 'last_name', 'address', 'fax', 'email', 'employee_id', 'reports_to', 'state'}
    
@pytest.fixture
def test_get_employee_total_sales():
    response = client.get("/employees/total_sales")
    assert response.status_code == 200