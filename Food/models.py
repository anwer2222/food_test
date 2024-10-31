
from django.db import models

class Pizza(models.Model):
    SHIRT_SIZES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large",
    }
     
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pizza_type = models.CharField(max_length=1, choices=SHIRT_SIZES,default='S')

    def __str__(self):
        return self.name

class Burger(models.Model):
    name = models.CharField('الاسم',max_length=100)
    ingredients = models.TextField("المحتوى")
    price = models.DecimalField("السعر",max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'برجر'
        verbose_name_plural = 'برجر'
    
class Macarona(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name