from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateAnnouncementForm,AcceptContactUSForm
from .models import Announcement,ContactUs
from django.http import Http404


def base_view(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def post(request):
    if request.method=="POST":
       form=CreateAnnouncementForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('posts')

    else:
       form=CreateAnnouncementForm()
    
    context={'form':form}
    return render(request,'announcements/create_post.html',context)

def post_list(request):
    posts=Announcement.objects.all().order_by('-createdAt')[:5]
    return render(request,'announcements/announcements.html', {"posts":posts})           


def updatePost(request,post_id):
    post=get_object_or_404(Announcement,id=post_id)
    if request.method =="POST":
        form =CreateAnnouncementForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
    else:
        form =CreateAnnouncementForm(instance=post)
    
    return render(request,'announcements/update_post.html',{'post':post,'post_id':post_id})

def deletePost(request,post_id):
    post=get_object_or_404(Announcement,id=post_id)
    post.delete()
    return redirect('announcements:posts')
    


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
