from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    mobile = models.CharField(max_length=30, null=True)
    class_standard = models.CharField(max_length=225, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(null=True, auto_now=True)