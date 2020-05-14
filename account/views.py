from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from account.forms import RegistrationForm,AccountAuthenticationForm
from django.template import loader
from django.http import HttpResponse
import core.models

#import account.models

# Create your views here.


def registration_view(request):
            
    context={}
    if request.POST:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            email=form.cleaned_data.get('email')
            
            raw_password=form.cleaned_data.get('password1')

            account=authenticate(email=email,password=raw_password)
            
            login(request,account)
            return redirect('core_index')
        
        else:
            context['registration_form']=form

    else:
        form=RegistrationForm()
        context['registration_form']=form
    #return render(request,'register.html',context)
    return render(request, 'register.html',context)


def logout_view(request):
    logout(request)
    return redirect('core_accueil')


def login_view(request):
    context={}
    
    if request.POST:
        form=AccountAuthenticationForm(request.POST)
        if form.is_valid():
            user=request.user
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(email=email,password=password)
            
            login(request,user)
            if user.is_authenticated:
                return redirect('core_articles')
        else:
            context['login_form']=form
    
    else:
        form=AccountAuthenticationForm()
        context['login_form']=form
    
    return render(request,'login.html',context)

'''
def login_view(request):
    context={}
    
    user=request.user
    
    if user.is_authenticated:
        
        return redirect('core_accueil')
    
    if request.POST:
        form=AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(email=email,password=password)
            
            if user:
                login(request,user)
                return redirect('core_articles')
    
    else:
        form=AccountAuthenticationForm()
        
    context['login_form']=form
    
    return render(request,'login.html',context)
    
''' 
    
    
    
    
    
    
    
    
    
    
    