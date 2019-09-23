from django.db import models
from user.models import User
from assets.models import Assets


class Perm(models.Model):
    name = models.CharField(max_length=30, unique=True)
    user = models.ManyToManyField(User)
    asserts = models.ManyToManyField(Assets)
    remark = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{},{}'.format(self.id, self.name)



