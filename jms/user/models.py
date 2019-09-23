from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
#    objects = models.Manager()
    name = models.CharField(max_length=32)
    wechat = models.CharField(max_length=128)

    def __str__(self):
        return '{}'.format(self.name)
