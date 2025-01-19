from django import forms
from .models import Birth,IdentificationCard,Mirrage,Supportive

class BirthForm(forms.ModelForm):
    class Meta:
        model=Birth
        fields=['childName','gender','fatherName','motherName','birthDate',
                'file']



class IdentificatioCardForm(forms.Form):
    class Meta:
        model=IdentificationCard
        fields=[
            'firstName','middleName','lastName','age','gender','houseNumber'
        ]
       

class MirrageForm(forms.Form):
    class Meta:
        model=Mirrage
        fields=[
            'groomName','brideName','widdingDate']
  
class SupportivePaper(forms.Form):
    class Meta:
        fields=[
            'firstName','lastName','age','kebeleId','gender','reason'
        ]


