# models.py
from django.contrib.auth.models import User,AbstractUser
from django.db import models


class ResidentialID(models.Model):
    id_number = models.CharField(max_length=20, unique=True)
    used = models.BooleanField(default=False)  

    def __str__(self):
        return self.id_number

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    residential_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.user.username
    

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('resident', 'Resident'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='resident')

    groups = models.ManyToManyField(
        'auth.Group', related_name='customuser_groups', blank=True, help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='customuser_permissions', blank=True, help_text='Specific permissions for this user.'
    )

class FeedBack(models.Model):
    department =models.CharField(max_length=20)
    message=models.TextField()
