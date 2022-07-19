from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=60)
    firstname = models.CharField(max_length=60)
    mail = models.EmailField(max_length=254)
    pwd = models.CharField(max_length=254)


class Games(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    data = models.CharField(max_length=2000)