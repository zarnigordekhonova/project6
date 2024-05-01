from django.urls import path
from products.views import get_product_info

urlpatterns = [
    path('', get_product_info)
]