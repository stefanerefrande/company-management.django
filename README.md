## Company Management app

![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg) 

# Description
This project is a simple Django REST API where we can access and create different companies´s directories and its employees. Each company can have more than one employee, and each employee can be related to more than one company. This organization was implemented through Django´s [Many to Many Relationship](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/) models.

# Endpoints
/employees -> brings up a list of employees and the company or companies they are related to <br>
/company -> brings up a list of registered companies and its employees

# Requirements
- Python (version 3.9.0)
- Django Rest Framework

# Postman
The application´s endpoints can also be accessed through Postman, [as is shown here.](https://github.com/stefanerefrande/company-management.django/tree/main/CompanyManagement/readme_images)
![company_list](https://github.com/stefanerefrande/company-management.django/blob/main/CompanyManagement/readme_images/Captura%20de%20Tela%202021-10-15%20%C3%A0s%2019.09.26.png?raw=true)
