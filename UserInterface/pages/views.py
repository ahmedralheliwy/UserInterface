from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing(request):
    return render(request, 'pages/landing.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'pages/home.html')