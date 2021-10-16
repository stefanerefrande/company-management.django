from rest_framework import serializers
from .models import Employees, Company


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('employee_id', 'employee_name', 'employee_username')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_id', 'company_name', 'virtual_address', 'employee')
