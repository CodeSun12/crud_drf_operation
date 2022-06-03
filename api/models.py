from django.db import models
import rest_framework


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    roll_number = models.IntegerField()
    degree = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
