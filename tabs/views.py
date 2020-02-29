from django.shortcuts import render,redirect
from .models import Tab
from. import form
# Create your views here.
from .form import TabForm

def addTab(request):
    if request.method == 'POST':
        form = TabForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TabForm()
    return render(request, 'addTab.html', {'form': form})

def showTab(request):
    tabs=Tab.objects.all()
    return  render(request,'showTab.html',{'tabs':tabs})
