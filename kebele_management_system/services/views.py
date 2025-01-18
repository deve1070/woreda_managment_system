from django.shortcuts import render
from .forms import BirthForm,MirrageForm,IdentificatioCardForm,SupportivePaper
from .models import Birth,Mirrage,IdentificationCard,Supportive
from django.http import FileResponse,Http404

def index(request):
    return render(request,'service.html')


def applyBirth(request):
    if request.method=='POST':
        form=BirthForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            applicant=request.user
        else:
            return render(request,'birth.html',{'form':form})
    else:
        form=BirthForm()
    
    return render(request,'birth.html',{'form':form})

def applyMirrage(request):
    if request.method=='POST':
        form=MirrageForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.applicant=request.user
            form.save()
        else:
            return render(request,'mirrage.html', {'form':form})
    else:
        form=MirrageForm()
    
    return render(request,'mirrage.html',{'form':form})


def issueId(request):
    if request.method=='POST':
        form=IdentificatioCardForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.applicant=request.user
            form.save()
        
        else:
            return render(request,'issueId.html',{'form':form})
    

    else:
        form=IdentificatioCardForm()

    return render(request,'issueId.html',{'form':form})


def supportivePaper(request):
    if request.method=='POST':
        form=SupportivePaper(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.applicant=request.user
            form.save()
        
        else:
            return render(request,'supportive.html',{'form':form})
    else:
        form=SupportivePaper()
        return render(request,'supportive.html',{'form':form})
    

def serviceRequest(request):
    birth_pending_requests=Birth.objects.filter(status='pending').order_by('createdAt')
    mirrage_pending_requests=Mirrage.objects.filter(status='pending').order_by('createdAt')
    issueId_pending_requests=IdentificationCard.objects.filter(status='pending').order_by('createdAt')
    supportive_pending_requests=Supportive.objects.filter(status='pending').order_by('createdAt')

    context={
        'births': birth_pending_requests,
        'mirrages':mirrage_pending_requests,
        'idissues': issueId_pending_requests,
        'supportives': supportive_pending_requests
        }
    return render(request,'serviceRequests.html',context)

def download_file(request,file_id):
    try:
        birth_certificate_request=Birth.objects.get(id=file_id)
        file_path=birth_certificate_request.file.path
        return FileResponse(open(file_path,'rb'), as_attachment=True,filename=birth_certificate_request.file.name)

    except Birth.DoesNotExist:
        raise Http404('file not found')
    except Exception as e:
        raise Http404(f"Error:{e}")

def upadteStatus(request,request_id):
    servicerequest=



