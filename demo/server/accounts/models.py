from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=200, blank=True, null=True)
    avatar = models.ImageField(
        upload_to='uploads/%Y%m/%d', blank=True, null=True
    )
