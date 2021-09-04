from django.shortcuts import render

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