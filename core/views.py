from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def otp(request):
    return render(request, 'otp.html')