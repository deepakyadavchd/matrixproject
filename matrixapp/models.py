from django.db import models


# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=70)
    gender=models.CharField(max_length=50)
    hobby=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    

    def __str__(self):
        return self.name