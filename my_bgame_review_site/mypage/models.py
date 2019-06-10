from django.db import models


# Create your models here.
class MyStatus(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    hobby = models.TextField()

