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

# Virtualenv
You can create a virtualenv in two ways, using: `Python default virtualenv` or `Poetry virtualenv`. Feel free to choose which one you prefer.
----> Python Virtualenv
Create a virtualenv and activate it.
```sh
python -m venv .venv
source .venv/bin/activate
```

----> Poetry Virtualenv
Create a virtualenv and activate it.
```sh
poetry shell
```
# Run the application
To run the application in development mode, execute the command below. It'll up the project and expose it on the url `http://localhost:8000`
```sh
make run
```
# Postman
The application´s endpoints can also be accessed through Postman:

# Heroku
CLick here to check the application deployed at Heroku´s platform.
