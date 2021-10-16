from ..serializers import EmployeesSerializer, CompanySerializer


def test_employee_serializer():
    request_data = {
        "employee_id": 1,
        "employee_name": "Anna",
        "employee_username": "annameyer",
        "company": "Company Hero"
    }
    serializer = EmployeesSerializer(request_data)
    assert serializer.data == {
        "employee_id": 1,
        "employee_name": "Anna",
        "employee_username": "annameyer",
        "company": "Company Hero"
    }


def test_company_serializer():
    request_data = {
        "company_id": 2,
        "company_name": "Google",
        "virtual_address": "California",
        "employee": [1, 2]
    }
    serializer = CompanySerializer(request_data)
    assert serializer.data == {
        "company_id": 2,
        "company_name": "Google",
        "virtual_address": "California",
        "employee": [1, 2]
    }