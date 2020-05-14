from django.contrib import admin
from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from . import views
from django.conf.urls import url, include

from core import views as core
from account import views as account

from account.views import(
        registration_view,
        logout_view,
        login_view,
        )

urlpatterns = [
        
    path('admin/', admin.site.urls),
    path('index' , core.index, name = 'core_index'),
    #path('', core.connection, name = 'core_connection'),
    
    path('contact', core.contact, name='core_contact'),
    
    #path('citoyen', core.citoyen, name='core_citoyen'),
    
    path('', core.accueil, name='core_accueil'),
    path('articles', core.articles, name='core_articles'),
    
    path('register/',registration_view,name="register"),
    
    path('logout/',logout_view,name="logout"),
    path('login/',login_view,name="login"),
    
    
    
    #re_path(r'(?P<p_url>[a-zA-Z0-9_.,-]+)', core.page, name='core_page'),
    
    #views.url(r'^about/$',views.about),
    #views.url(r'^$',views.homepage),
    
]

urlpatterns += staticfiles_urlpatterns()