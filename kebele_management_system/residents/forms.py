# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import ResidentialID,CustomUser,Profile

class RegistrationForm(forms.ModelForm):
    residential_id = forms.CharField(max_length=20, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'residential_id']

    def save(self, commit=True):
        user = super().save(commit=False)
        residential_id = self.cleaned_data.get('residential_id')

        # Set the role to resident
        user.role = 'resident'
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

            # Mark the Residential ID as used
            ResidentialID.objects.filter(id_number=residential_id).update(used=True)

            # Create a Profile with the residential ID
            Profile.objects.create(user=user, residential_id=residential_id)

        return user

