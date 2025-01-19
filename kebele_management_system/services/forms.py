from django import forms
from .models import Birth,IdentificationCard,Mirrage,Supportive

class BirthForm(forms.ModelForm):
    class Meta:
        model=Birth
        fields=['childName','gender','fatherName','motherName','birthDate',
                'file']



class IdentificatioCardForm(forms.ModelForm):
    class Meta:
        model=IdentificationCard
        fields=[
            'firstName','middleName','lastName','age','gender','houseNumber'
        ]
       

class MirrageForm(forms.ModelForm):
    class Meta:
        model=Mirrage
        fields=[
            'groomName','brideName','widdingDate']
  
class SupportivePaper(forms.ModelForm):
    class Meta:
        model=Supportive
        fields=[
            'firstName','lastName','age','kebeleId','gender','reason'
        ]


