from django.shortcuts import render



def post(request):
    if request.method=="post":
        form=postCreationForm(request.POST)
        form.poster=request.user
        if form.is_valid():
            form.save()
    else:
        form=postCreationForm()


    context={'form':form}
    return render(request,)

# Create your views here.
