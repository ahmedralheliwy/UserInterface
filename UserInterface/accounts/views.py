from django.shortcuts import render,redirect
from .forms import UserRegisterForm, UserLoginForm

#For Authentication
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
#Use auth_login instead of login to avoid naming conflict

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method=='POST':
        form=UserLoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request,user)
                next_url=request.GET.get('next','home')
                return redirect(next_url)
            else:
                form.add_error(None,'Invalid username of password')
    else:
        form=UserLoginForm()
    return render(request, 'accounts/login.html', {'form':form})

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return redirect('landing')

@login_required(login_url='login')
def details(request):
    return render(request, 'accounts/details.html')