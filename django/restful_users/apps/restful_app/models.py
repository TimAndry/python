from __future__ import unicode_literals
from django.db import models



class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add = True)




