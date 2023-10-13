from django.urls import path
from .views import products_list,create_product,update_Product,delete_Product

urlpatterns = [
    path('product_list/',products_list,name='products_list'),
    path('product_list/create',create_product,name="createProduct"),
    path('product_list/update/<int:id>',update_Product,name="updateProduct"),
    path('product_list/delete/<int:id>',delete_Product,name="deleteProduct"),
]