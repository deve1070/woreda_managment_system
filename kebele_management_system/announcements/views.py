from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateAnnouncementForm,AcceptContactUSForm
from .models import Announcement,ContactUs


def post(request):
    if request.method=="POST":
       form=CreateAnnouncementForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('home.html')

    else:
       form=CreateAnnouncementForm()
    
    context={'form':form}
    return render(request,'create_post.html',context)

def post_list(request):
    posts=Announcement.objects.get().order_by('-createdAt')[:5]
    return render(request,'announcements.html', {"posts":posts})           


def updatePost(request,post_id):
    post=get_object_or_404(Announcement,id=post_id)
    if request.method =="POST":
        form =CreateAnnouncementForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
    else:
        form =CreateAnnouncementForm(instance=post)
    
    return render(request,'post_update',{'post':post})

def deletePost(request,post_id):
    post=Announcement.objects.get(id=post_id)
    post.delete()



def contactUs(request):
    if request.method=='POST':
        form=AcceptContactUSForm(request.POST)
        if form.is_valid():
            form.save()
        
        else:
            return render(request,'contact.html',{'form':form})
    else:
        form=AcceptContactUSForm()
    
    return render(request,'contact.html',{'form':form})
