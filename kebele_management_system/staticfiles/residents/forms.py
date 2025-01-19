# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import ResidentialID,CustomUser

class RegistrationForm(forms.ModelForm):
    residential_id = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'residential_id']

    def clean_residential_id(self):
        residential_id = self.cleaned_data.get('residential_id')

        # Check if the residential ID exists in the ResidentialID model
        if not ResidentialID.objects.filter(id_number=residential_id).exists():
            raise forms.ValidationError("Invalid Residential ID. You cannot register.")

        # Check if the residential ID is already used
        if ResidentialID.objects.filter(id_number=residential_id, used=True).exists():
            raise forms.ValidationError("This Residential ID is already used. You cannot register again.")

        return residential_id

class ResidentRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'resident'
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

