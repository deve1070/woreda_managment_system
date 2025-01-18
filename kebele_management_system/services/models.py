from django.db import models
from django.contrib.auth.models import User

class Birth(models.Model):
    GENDER_CHOICES=[
        ('M', 'Male'),
        ('F', 'Famale'),]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    childName=models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    fatherName=models.CharField(max_length=200)
    motherName=models.CharField(max_length=200)
    birthDate=models.DateTimeField()
    file=models.FileField(upload_to='assets/')
    applicant=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    createdAt=models.DateTimeField(auto_now_add=True)
    updateAt=models.DateTimeField(auto_now=True)


class IdentificationCard(models.Model):
    GENDER_CHOICES=[
        ('M', 'Male'),
        ('F', 'Famale'),
           ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    firstName=models.CharField(max_length=200)
    middleName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    age=models.IntegerField()
    houseNumber=models.CharField(max_length=15)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    applicant=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    createdAt=models.DateTimeField(auto_now_add=True)
    updateAt=models.DateTimeField(auto_now=True)

class Mirrage(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    groomName=models.CharField(max_length=200)
    brideName=models.CharField(max_length=200)
    widdingDate=models.DateTimeField()
    applicant=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    createdAt=models.DateTimeField(auto_now_add=True)
    updateAt=models.DateTimeField(auto_now=True)

class Supportive(models.Model):
    GENDER_CHOICES=[
        ('M', 'Male'),
        ('F', 'Famale'),
        ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    firstName=models.CharField(max_length=200)
    middleName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    age=models.IntegerField()
    kebeleId=models.CharField(max_length=10)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    reason=models.TextField()
    applicant=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    createdAt=models.DateTimeField(auto_now_add=True)
    updateAt=models.DateTimeField(auto_now=True)

