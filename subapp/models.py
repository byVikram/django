from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class hello(models.Model):
    first = models.CharField(max_length=50)
    num = models.IntegerField()

class newtable(models.Model):
    column1 = models.CharField(max_length=50,null=True)
    column2 = models.CharField(max_length=50,null=True)