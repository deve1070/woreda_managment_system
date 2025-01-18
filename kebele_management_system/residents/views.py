from django.shortcuts import render
from django.contrib.auth import authenticate, login



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
