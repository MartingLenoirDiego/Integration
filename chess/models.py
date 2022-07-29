from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


class Games(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data = models.CharField(max_length=2000)
    date = models.DateField(default=datetime.now)



