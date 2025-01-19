from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from .models import ResidentialID,Profile


def my_login_view(request):
    if request.method=='POST':
        usrname=request.POST['usrname']
        password=request.POST['password']

        user=authenticate(request, usrname=usrname, password=password)
        if user is not None:
            login(request,user)
            return render 
        else:
            render(request,'login.html',{'error':'Invalid credentials'})

    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Save the residential ID in the Profile model
            residential_id = form.cleaned_data['residential_id']
            Profile.objects.filter(user=user).update(residential_id=residential_id)

            # Mark the residential ID as used
            ResidentialID.objects.filter(id_number=residential_id).update(used=True)

            return redirect('login')  # Redirect to the login page
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

