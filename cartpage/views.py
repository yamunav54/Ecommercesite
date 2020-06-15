from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm
from django.contrib import messages


# Create your views here.
def homeview(request):
    return render(request,'home.html',{})

def loginview(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username Or Password is incorrect')


    context={}
    return render(request,'login.html',context)

def logoutuser(request):
    logout(request)
    return redirect('login')

def registerview(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for' + user)

    context={'form':form}
    return render(request,'register.html',context)

def storeview(request):
    context={}
    return render(request,'store.html',context)

def cartview(request):
    context={}
    return render(request,'cart.html',context)

def checkoutview(request):
    context={}
    return render(request,'checkout.html',context)