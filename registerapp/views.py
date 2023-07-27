from django.shortcuts import render,redirect
from registerapp.forms import RegisterForm
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def RegisterVW(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            password=form.password
            form.password=make_password(password)
            form.save()
            return HttpResponse('User Registered!')
    return render(request,'register.html',{'form':form})


def LoginVW(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/weather/')
        else:
            return HttpResponse('wrong password')
    return render(request,'login.html',{'form':form})

def LogOutVW(request):
    logout(request)
    return HttpResponse('logged out')