from django import forms
from .models import Announcement,ContactUs

class CreateAnnouncementForm(forms.ModelForm):
    class Meta:
        model=Announcement
        fields=['title','text','image','video']

class AcceptContactUSForm(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields='__all__'
        
        