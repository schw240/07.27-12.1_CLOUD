from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)

class Scores(models.Model):
    name = models.CharField(max_length=10)
    math = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    english = models.IntegerField(default=0)