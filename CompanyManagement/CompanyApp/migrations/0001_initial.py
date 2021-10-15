# Generated by Django 3.2.8 on 2021-10-15 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_username', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=300)),
                ('virtual_address', models.CharField(max_length=300)),
                ('employee', models.ManyToManyField(to='CompanyApp.Employees')),
            ],
        ),
    ]
