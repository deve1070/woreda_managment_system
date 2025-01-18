from django.db import models
from django.contrib.auth.models import User


class resident(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture =models.ImageField(upload_to='image')
