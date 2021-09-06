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
        pass
    else:
        return render(request,'index.html')
def contact(request):
    if request.method == 'POST':
        pass
    else:
        return render(request,'contact.html')
def pending(request):
    if request.method == 'POST':
        pass
    else:
        context = {'orders':Order.objects.all()}
        return render(request,'pending.html',context)