from django.urls import path
from customers.views import get_info_customer

urlpatterns = [
    path('', get_info_customer)
]