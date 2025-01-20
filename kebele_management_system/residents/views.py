from django.shortcuts import render,redirect
from django.contrib.auth import  login as auth_login
from .forms import RegistrationForm
from .models import ResidentialID,Profile,FeedBack
from django.contrib.auth.forms import AuthenticationForm


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()

            # Check the user's role and redirect accordingly
            if user.role == 'admin':
                auth_login(request, user)  # Use Django's login system
                return redirect('admin:index')  # Redirect to admin dashboard
            elif user.role == 'staff':
                auth_login(request, user)  # Allow staff login
                return redirect('home')  # Redirect to staff home or dashboard
            elif user.role == 'resident':
                auth_login(request, user)  # Log in resident
                return redirect('home')  # Redirect to the resident's home page
            else:
                form.add_error(None, "Invalid user role.")
        else:
            form.add_error(None, "Invalid credentials.")
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Profile, ResidentialID

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Handle the residential ID
            residential_id = form.cleaned_data['residential_id']
            
            # Check if the residential_id is already used
            residential_id_obj = ResidentialID.objects.filter(id_number=residential_id).first()
            if residential_id_obj and residential_id_obj.used:
                form.add_error('residential_id', 'This residential ID has already been used.')
                return render(request, 'registration/register.html', {'form': form})

            # Update the Profile with the residential ID
            Profile.objects.filter(user=user).update(residential_id=residential_id)
            
            # Mark the residential ID as used
            if residential_id_obj:
                residential_id_obj.used = True
                residential_id_obj.save()

            # Redirect to home page after successful registration
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def giveFeedBack(request):
    if request.method=="POST":
        form=FeedBack(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=FeedBack()
    
    return render(request,'residents/feedback.html',{'form':form})

