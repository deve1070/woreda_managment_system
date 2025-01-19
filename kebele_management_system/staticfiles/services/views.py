from django.shortcuts import render,get_object_or_404,redirect
from .forms import BirthForm,MirrageForm,IdentificatioCardForm,SupportivePaper
from .models import Birth,Mirrage,IdentificationCard,Supportive
from django.http import FileResponse,Http404,JsonResponse

def index(request):
    return render(request,'services/index.html')


def applyBirth(request):
    if request.method=='POST':
        form=BirthForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            applicant=request.user
        else:
            return render(request,'services/birth.html',{'form':form})
    else:
        form=BirthForm()
    
    return render(request,'services/birth.html',{'form':form})

def applyMirrage(request):
    if request.method=='POST':
        form=MirrageForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.applicant=request.user
            form.save()
        else:
            return render(request,'services/mirrage.html', {'form':form})
    else:
        form=MirrageForm()
    
    return render(request,'services/mirrage.html',{'form':form})


def issueId(request):
    if request.method=='POST':
        form=IdentificatioCardForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.applicant=request.user
            form.save()
        
        else:
            return render(request,'services/issueId.html',{'form':form})
    

    else:
        form=IdentificatioCardForm()

    return render(request,'services/issueId.html',{'form':form})


def supportivePaper(request):
    if request.method=='POST':
        form=SupportivePaper(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.applicant=request.user
            form.save()
        
        else:
            return render(request,'services/supportive.html',{'form':form})
    else:
        form=SupportivePaper()
        return render(request,'services/supportive.html',{'form':form})
    

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
    return render(request,'services/serviceRequests.html',context)

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
    if request.method=='POST':
        status =request.POST.get('status')
        bithService=get_object_or_404(Birth, id=request_id)
        mirrageService=get_object_or_404(Birth, id=request_id)
        idissueService=get_object_or_404(Birth, id=request_id)
        supportiveService=get_object_or_404(Birth, id=request_id)

        bithService.status=status
        mirrageService.status=status
        idissueService.status=status
        supportiveService.status=status

        bithService.save()
        mirrageService.save()
        idissueService.save()
        supportivePaper.save()

        return JsonResponse({'message':'Stataus updated successfully','status':status})
    return JsonResponse({'error':'Unauthorized'},status=403)







