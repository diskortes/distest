from django.db import models

class MyData(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    bio = models.TextField()
    email= models.CharField(max_length=20)

class META_Data(models.Model):
    ip = models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    date=models.DateField()
