from django.urls import path
from .views import doctor_list,create_doctor,Update_doctor,Delete_doctor

urlpatterns = [
    path('doctor_list/',doctor_list,name='doctors_list'),
    path('doctor_list/create',create_doctor,name='create_doctor'),
    path('doctor_list/update/<int:id>',Update_doctor,name='update_doctor'),
    path('doctor_list/delete/<int:id>',Delete_doctor,name='delete_doctor'),
]