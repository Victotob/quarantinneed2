# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:17:19 2020

@author: nicob
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):
    '''
    email=          forms.EmailField(max_length=60)
    username =      forms.CharField(max_length = 30)
    nbPersonnes=    forms.IntegerField()
    nomsPersonnes=  forms.CharField(max_length = 128)
    numTel =        forms.CharField(max_length = 128)
    '''
    
    class Meta:
        model=Account
        fields=('email','nbPersonnes','nomsPersonnes','numTel','adresse','codepostal','ville','pays','username','password1','password2')


class AccountAuthenticationForm(forms.ModelForm):
    
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    
    class Meta:
        model=Account
        fields=('email','password')
        
    def clean(self):
        email=self.cleaned_data['email']
        password=self.cleaned_data['password']
        if not authenticate(email=email,password=password):
            raise forms.ValidationError("Invalid email !!!")