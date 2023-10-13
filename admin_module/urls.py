from django.urls import path
from .views import user,appointments_view,employee_data_view,register,deals_view,updateEmployee

urlpatterns = [
    path('',user,name='admin'),
    path('appointments/',appointments_view,name='appointments'),
    path('employee_data/',employee_data_view,name='employee'),
    path('employee_data/create',register,name='create_employee'),
    path('employee_data/update/<int:id>',updateEmployee,name='update_employee'),
    path('deals/',deals_view,name='Emp_deals'),
]