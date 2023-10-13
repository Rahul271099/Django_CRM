from django.urls import path
from .views import deals_list,create_deals

urlpatterns = [
    path('deals/',deals_list,name='deals_list'),
    path('deals/create',create_deals,name='create_deal'),
]