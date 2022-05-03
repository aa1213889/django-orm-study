from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    size = models.IntegerField(default=0)
    email = models.CharField(max_length=32, null=True, blank=True)
