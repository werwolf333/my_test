from django.urls import path
from . import views


app_name = 'employee'

urlpatterns = [
    path('all', views.AllEmployee.as_view()),
    path('level_<int:level>', views.EmployeeLevel.as_view()),
]

