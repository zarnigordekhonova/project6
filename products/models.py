from django.db import models

# Create your models here.


class product_info(models.Model):
    name = models.CharField(max_length=255)
    weight = models.IntegerField()
    color = models.CharField(max_length=255)
    size = models.IntegerField()


    def __str__(self):
        return f'{self.name} {self.color}'


class booking_product(models.Model):
    number = models.IntegerField()
    type_payment = models.CharField(max_length=255)
    price = models.IntegerField()
    delivery_time = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.number} {self.price}'