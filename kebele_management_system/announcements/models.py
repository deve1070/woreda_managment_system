from django.db import models

class Announcement(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    image=models.ImageField(upload_to='image',blank=True,null=True)
    video=models.FileField(upload_to='video')
    createdAt=models.DateTimeField(auto_now_add=True)
    updateAt=models.DateTimeField(auto_now=True)
    # poster=models.ForeignKey()


    def __str__(self):
        return "{self.title}\n {self.text}"
# Create your models here.
