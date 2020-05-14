from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import core.models

def index(request):
    template = loader.get_template('index.html')
    context = {'index' : index
               }
    #return HttpResponse('Bienvenue sur notre projet QuarantinNeed')
    return HttpResponse(template.render(context, request))



def page(request, p_url):
    core.models.template = loader.get_template('page.html')
    try:
        page = core.models.Page.objects.get(p_adresse = p_url)
    except:
        page = core.models.Page.objects.none()
        page.p_contenu = "<h1>Erreur la page demandée n'existe pas</h1>"
        
    core.models.context = {
            'page' : page,
            }

def citoyen(request,):
    template = loader.get_template('page.html')
    page = core.models.Page.objects.none()
    page.p_titre = "Interface citoyen"
    page.p_description = "Fonctionnalités citoyen"
    page.p_contenu = "<p>Connectez vous ou créez votre compte.</p>"
    
    context = {
        'page' : page,
    }
    return HttpResponse(template.render(context, request))


def accueil(request,):
    template = loader.get_template('page.html')
    page = core.models.Page.objects.none()
    
    context = {
        'page' : page,
    }
    return HttpResponse(template.render(context, request))
    

def contact(request,):
    template = loader.get_template('page.html')
    page = core.models.Page.objects.none()
    page.p_titre = "Inscription chez Quarant'In Need"
    page.p_description = "Formulaire d'inscription"
    page.p_contenu = "<p>Merci de remplir tous les champs.</p>"
    page.p_adresse = "/contact"
    
    if request.method == "POST":
        form = core.models.ContactForm(request.POST)
        core.models.n_contact = form.save()
        page.p_contenu = "<p>Bravo, vous êtes désormais inscrit !</p>"

    else:
        form = core.models.ContactForm()
    
    context = {
        'page' : page,
        'form' : form,
    }
    return HttpResponse(template.render(context, request))

def articles(request,):
    template = loader.get_template('page.html')
    
    page = core.models.Page.objects.none()
    page.p_titre="Gestion de votre commande"
    page.p_description= "Articles composant votre commande"
    page.p_contenu = "<p>Vous retrouverez dans cette page le suivi des articles commandés</p>"
    page.p_adresse = "/articles"
    
    if request.method == "POST":
        form = core.models.ArticlesForm(request.POST)
        core.models.n_articles = form.save()
        page.p_contenu = "<p>Merci. Nous avons pris en compte votre commande.</p>"

    else:
        form = core.models.ArticlesForm()
    
    context = {
            'page' : page,
            'form':form,
            }
    return HttpResponse(template.render(context, request))