from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def join(request):
    return render(request, 'JoinUs.html')

def webportal(request):
    return render(request, 'webportal.html')
