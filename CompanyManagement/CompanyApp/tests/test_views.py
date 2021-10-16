import json
import pytest
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Employees, Company
from ..serializers import EmployeesSerializer, CompanySerializer


# initialize the APIClient app
client = Client()


@pytest.fixture
def employees_valid_payload():
    return {
        'employee_id': 1,
        "employee_name": "Anna",
        "employee_username": "annameyer",
        "company": "Company Hero"
    }


@pytest.fixture
def employees_invalid_payload():
    return {
        'employee_id': "",
        "employee_name": "Anna",
        "employee_username": "",
        "company": ""
    }


@pytest.fixture
def company_valid_payload():
    return {
        'company_id': 2,
        "company_name": "Google",
        "virtual_address": "California",
        "employee": [1, 2]
    }


@pytest.fixture
def company_invalid_payload():
    return {
        'company_id': "",
        "company_name": "",
        "virtual_address": "California",
        "employee": []
    }


class GetAllEmployeesTest(TestCase):

    def setUp(self):
        Employees.objects.create(
            employee_id=1, employee_name='Anna', employee_username='annameyer', company='Company Hero')
        Employees.objects.create(
            employee_id=2, employee_name='James', employee_username='jamesbrown', company='Google')

    def test_get_all_experiments(self):
        # get API response
        response = client.get(reverse('get_post_employees'))
        # get data from db
        employee = Employees.objects.all()
        serializer = EmployeesSerializer(employee, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllCompaniesTest(TestCase):

    def setUp(self):
        Company.objects.create(
            company_id=1, company_name='Company Hero', virtual_address='São Paulo', employee=[1, 2])
        Company.objects.create(
            company_id=2, company_name='Google', virtual_address='California', employee=[2, 3])

    def test_get_all_companies(self):
        # get API response
        response = client.get(reverse('get_post_companies'))
        # get data from db
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewEmployee(TestCase):

    def test_should_create_valid_employee(self):
        response = client.post(
            reverse('get_post_employees'),
            data=json.dumps(employees_valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_create_invalid_employee(self):
        response = client.post(
            reverse('get_post_employees'),
            data=json.dumps(employees_invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CreateNewCompany(TestCase):

    def test_create_valid_company(self):
        response = client.post(
            reverse('get_post_company'),
            data=json.dumps(company_valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_company(self):
        response = client.post(
            reverse('get_post_company'),
            data=json.dumps(company_invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateEmployeeTest(TestCase):

    def setUp(self):
        self.project = Employees.objects.create(
            employee_id=1, employee_name='Anna', employee_username='annameyer', company='Company Hero'
        )
        self.project2 = Employees.objects.create(
            employee_id=2, employee_name='James', employee_username='jamesbrown', company='Google')

    def test_valid_update_employee(self):
        response = client.put(
            reverse('get_delete_update_employee', kwargs={'pk': self.project2.pk}),
            data=json.dumps(employees_valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_employee(self):
        response = client.put(
            reverse('get_delete_update_experiment', kwargs={'pk': self.project2.pk}),
            data=json.dumps(employees_invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateCompanyTest(TestCase):

    def setUp(self):
        self.project = Company.objects.create(
            company_id=1, company_name='Company Hero', virtual_address='São Paulo', employee=[1, 2])
        self.project2 = Company.objects.create(
            company_id=2, company_name='Google', virtual_address='California', employee=[2, 3])

    def test_valid_update_company(self):
        response = client.put(
            reverse('get_delete_update_company', kwargs={'pk': self.project2.pk}),
            data=json.dumps(company_valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_company(self):
        response = client.put(
            reverse('get_delete_update_company', kwargs={'pk': self.project2.pk}),
            data=json.dumps(company_invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteEmployeesTest(TestCase):

    def setUp(self):
        self.project = Employees.objects.create(
            employee_id=1, employee_name='Anna', employee_username='annameyer', company='Company Hero'
        )
        self.project2 = Employees.objects.create(
            employee_id=2, employee_name='James', employee_username='jamesbrown', company='Google')

    def test_valid_delete_employee(self):
        response = client.delete(
            reverse('get_delete_update_employee', kwargs={'pk': self.project2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_employee(self):
        response = client.delete(
            reverse('get_delete_update_employee', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class DeleteCompanyTest(TestCase):

    def setUp(self):
        self.project = Company.objects.create(
            company_id=1, company_name='Company Hero', virtual_address='São Paulo', employee=[1, 2])
        self.project2 = Company.objects.create(
            company_id=2, company_name='Google', virtual_address='California', employee=[2, 3])

    def test_valid_delete_company(self):
        response = client.delete(
            reverse('get_delete_update_company', kwargs={'pk': self.project2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_company(self):
        response = client.delete(
            reverse('get_delete_update_company', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)