from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/new/', product_form, name='product_form'),
    path('product/<int:id>/edit/', product_form, name='product_form'),
    path('product/<int:id>/delete/', delete_product, name='delete_product'),
]
