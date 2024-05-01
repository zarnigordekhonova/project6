from django.contrib import admin
from products.models import product_info, booking_product

# Register your models here.

admin.site.register(product_info)
admin.site.register(booking_product)
