from django.urls import path
from .views import appointment_list,create_appointment

urlpatterns = [
    path('appointment-list/',appointment_list,name='appointment_list'),
    path('appointment-list/create',create_appointment,name='create_appointment'),
]