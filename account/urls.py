# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:00:35 2020

@author: nicob
"""
from django.contrib import admin
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
from django.urls import path
app_name="account"

from account.views import(
        registration_view,
        )

from core.views import(
        index,
        )


urlpatterns=[
        path('admin/', admin.site.urls),
        path('',index,name="home"),
        path('register/',registration_view,name="register"),
        ]
