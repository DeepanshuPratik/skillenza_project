from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        pass
    else:
        return render(request,'index.html')
        
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        index = Index(name=name, subject = subject, email = email, message = message)
        index.save()
        return render(request,'index.html')
    else:
        return render(request,'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, subject = subject, message = message)
        contact.save()
        return render(request,'contact.html')
    else :
        return render(request,'contact.html')

def pending(request):
    if request.method == 'POST':
        pass
    else:
        context = {'orders':Order.objects.all()}
        return render(request,'pending.html',context)