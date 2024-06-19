from django.urls import path
from . import views

app_name = 'plp_ecommerce_app'

urlpatterns = [
    path('', views.product_list, name='product_list'),
]