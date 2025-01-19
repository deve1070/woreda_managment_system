from django.db import models

class Announcement(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    image=models.ImageField(upload_to='assets',blank=True,null=True)
    video=models.FileField(upload_to='assets',blank=True,null=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    updateAt=models.DateTimeField(auto_now=True)
    # poster=models.ForeignKey()


    def __str__(self):
        return f"{self.title},{self.text[:50]}"

class ContactUs(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()