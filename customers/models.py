from django.db import models

# Create your models here.

class customer_info1(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.name} {self.surname}'


class customer_info(models.Model):
    credit_card_number = models.IntegerField()
    phone_number = models.IntegerField()
    delivery_address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.credit_card_number} {self.phone_number}'
