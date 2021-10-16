from django.db import models


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    employee_username = models.CharField(max_length=50)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=300)
    virtual_address = models.CharField(max_length=300)
    employee = models.ManyToManyField(Employees, related_name='employee')
