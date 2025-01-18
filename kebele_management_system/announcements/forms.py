from django import forms
from .models import Announcement

class CreateAnnouncementForm(forms.Form):
    class Meta:
        model=Announcement
        fields=['title','text','image','video']
        