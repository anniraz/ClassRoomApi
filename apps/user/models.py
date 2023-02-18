from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email=models.EmailField()
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar=models.ImageField(upload_to='avatar/',null=True,blank=True)

    def __str__(self):
        return f"{self.username}"