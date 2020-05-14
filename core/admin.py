from django.contrib import admin
import core.models

def bt_p_bouillon(modeladmin, request, queryset):
    queryset.update(p_bouillon=False)
bt_p_bouillon.short_description = "Mode Bouillon actif"

class Page_Admin(admin.ModelAdmin):
    pass
    list_display = ('p_titre', 'p_adresse', 'p_bouillon',)
    list_filter = ('p_bouillon',)
    actions = [bt_p_bouillon]
admin.site.register(core.models.Page, Page_Admin)

class Contact_Admin(admin.ModelAdmin):
    pass
    list_display = ('c_name','c_nbPersonnes','c_nomsPersonnes','c_email','c_mdp','c_numTel','c_adresse','c_codepostal','c_ville','c_pays',)
    search_fields = ['c_name','c_nbPersonnes','c_nomsPersonnes','c_email','c_mdp','c_numTel','c_adresse','c_codepostal','c_ville','c_pays',]
    
admin.site.register(core.models.Contact, Contact_Admin)

class Articles_Admin(admin.ModelAdmin):
    pass
    list_display = ('a_statut','a_type','a_type2', 'a_type3','a_description',)
    search_fields = ['a_statut','a_type','a_type2', 'a_type3','a_description',]
    list_filter = ('a_statut','a_description',)
admin.site.register(core.models.Articles, Articles_Admin)