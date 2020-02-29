from django.db import models

# Create your models here.
class Phone(models.Model):
    name=models.CharField(max_length=200, default="Phone Name")
    brand=models.CharField(max_length=200, default="Brand Name")
    Camera=models.CharField(max_length=200, default="Camera Details")
    Processor =models.CharField(max_length=200, default="Processor Name")
    price =models.FloatField(max_length=200, default=0.00)
