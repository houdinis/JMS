from django.db import models


class Assets(models.Model):
    OS_TYPE = (
        ('C', 'Centos'),
        ('R', 'Redhat'),
        ('U', 'Ubuntu'),
        ('B', 'Bsd'),
        ('D', 'Debian'),
    )

    hostname = models.CharField(max_length=30, unique=True)
    ip = models.GenericIPAddressField(unique=True)
    port = models.IntegerField(default=22)
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    os = models.CharField(choices=OS_TYPE, default='C', max_length=4)
    activate = models.BooleanField(default=True)

    def __str__(self):
        return '{}:{}'.format(self.hostname, self.ip)
