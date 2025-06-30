from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    phone_number=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
def __str__(self):
    return self.name