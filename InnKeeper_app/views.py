from django.shortcuts import render

# Create your views here.

def landing_page(request):
    return render(request, 'Landing.html')

def dashboard(request):
    return render(request, 'Dashboard.html')

def login(request):
    return render(request, 'Login.html')