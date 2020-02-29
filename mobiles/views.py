from django.shortcuts import render,redirect
from .models import Phone
from. import form
# Create your views here.
from .form import PhoneForm

def addMobile(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PhoneForm()
    return render(request, 'addmobile.html', {'form': form})

def showMobile(request):
    phns=Phone.objects.all()
    return  render(request,'showmobile.html',{'phns':phns})
