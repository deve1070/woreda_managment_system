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
            Profile.objects.filter(user=user).update(residential_id=residential_id)
            ResidentialID.objects.filter(id_number=residential_id).update(used=True)

            # Redirect to login page
            return redirect('login')
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

