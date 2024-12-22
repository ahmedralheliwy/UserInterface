from django.shortcuts import render,redirect
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            #Or user=form.save() from contrib.auth.login
            #And login(request, user)
            #Then return redirect('home')
    else:
        form=UserRegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('login')

def details(request):
    return render(request, 'accounts/details.html')