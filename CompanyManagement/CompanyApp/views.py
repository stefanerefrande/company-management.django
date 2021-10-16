from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Employees, Company
from .serializers import EmployeesSerializer, CompanySerializer


@csrf_exempt
def employees_api(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeesSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST':
        employees_data = JSONParser().parse(request)
        employees_serializer = EmployeesSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(employee_id=employee_data['employee_id'])
        employees_serializer = EmployeesSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update")

    elif request.method == 'DELETE':
        employee = Employees.objects.get(employee_id=id)
        employee.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def company_api(request, id=0):
    if request.method == 'GET':
        company = Company.objects.all()
        company_serializer = CompanySerializer(company, many=True)
        return JsonResponse(company_serializer.data, safe=False)

    elif request.method == 'POST':
        company_data = JSONParser().parse(request)
        company_serializer = CompanySerializer(data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)

    elif request.method == 'PUT':
        company_data = JSONParser().parse(request)
        company = Company.objects.get(company_id=company_data['company_id'])
        company_serializer = CompanySerializer(company, data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update")

    elif request.method == 'DELETE':
        company = Company.objects.get(company_id=id)
        company.delete()
        return JsonResponse("Deleted successfully", safe=False)

