from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField("Name",max_length=200)
    email=models.EmailField()
    age=models.CharField("Age",max_length=3)
    phone=models.CharField("Phone",max_length=10)

def __str__(self):
    return self.name