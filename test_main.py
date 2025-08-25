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

def test_get_employee():
    response = client.get("/employees/")
    assert response.status_code == 200
    assert set(response.json()[0].keys()) == {'title', 'birth_date', 'phone', 'postal_code', 'hire_date', 'country', 'city', 'first_name', 'last_name', 'address', 'fax', 'email', 'employee_id', 'reports_to', 'state'}

def test_get_employee_total_sales():
    response = client.get("/employees/total_sales")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert set(response.json().keys()) == {'first_name', 'last_name', 'TotalSales'}

def test_get_employee_by_id():
    # Assuming employee with ID 1 exists
    response = client.get("/employees/employee/1")
    assert response.status_code == 200
    employee_data = response.json()
    assert employee_data['employee_id'] == 1
    assert set(employee_data.keys()) == {'title', 'birth_date', 'phone', 'postal_code', 'hire_date', 'country', 'city', 'first_name', 'last_name', 'address', 'fax', 'email', 'employee_id', 'reports_to', 'state'}

    # Test for non-existent employee
    response = client.get("/employees/employee/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Employee with id=999 not found"}

def test_get_employee_performance():
    request_payload = {
        "title": "Sales Support Agent",
        "invoice_date": "2009-01-01"
    }
    response = client.post("/employees/employee_performance", json=request_payload)
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert set(response.json().keys()) == {'employee_id', 'first_name', 'last_name', 'title', 'CustomersHandled', 'totalSales', 'AvgInvoiceValue'}

    request_payload_no_match = {
        "title": "NonExistentTitle",
        "invoice_date": "2009-01-01"
    }
    response_no_match = client.post("/employees/employee_performance", json=request_payload_no_match)
    assert response_no_match.status_code == 200
    assert response_no_match.json() == []