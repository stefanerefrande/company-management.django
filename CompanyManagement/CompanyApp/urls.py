from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^company$', views.company_api),
    url(r'^company/(?P<company_name>\d+/$)', views.company_api),

    url(r'^employee$', views.employees_api),
    url(r'^employee/(?P<employee_username>\d+/$)', views.employees_api),
]
