from django.db import models
from django.forms import ModelForm

from django.template.defaultfilters import slugify

class Page(models.Model): #Architecture pour les pages static et dynamique
    p_titre = models.CharField("Titre", max_length = 128, unique =True)
    p_titre_slugify = models.CharField("Titre Slugify", max_length = 128, blank = True, editable = False)
    p_adresse = models.CharField("Adresse", max_length =64)
    p_mots_clefs = models.CharField("Mots clés", max_length = 512, blank = True)
    p_description = models.TextField("Description")
    p_contenu = models.TextField("Contenu")
    p_bouillon = models.BooleanField("Bouillon", default = True)
    
    class Meta:
        verbose_name = 'Gestion des pages'
        verbose_name_plural = 'Gestion des pages'
        ordering = ['p_adresse']
        
    def save(self, *args, **kwargs):
        self.p_titre_slugify = slugify(self.p_titre)
        super(Page, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.p_titre
    def __str__(self):
        return '%s' % (self.p_titre)

class Contact(models.Model):
    
    c_name = models.CharField("Nom du foyer", max_length = 128)
    c_nbPersonnes = models.IntegerField("Nombre de personnes")
    c_nomsPersonnes = models.CharField("Noms des personnes", max_length = 128)
    c_email = models.EmailField("Votre email")
    c_mdp = models.CharField("Tapez votre mot de passe", max_length = 128)
    c_numTel = models.CharField("Numéro de téléphone", max_length = 128)
    c_adresse = models.CharField("Adresse", max_length = 128)
    c_codepostal = models.CharField("Code postal", max_length = 128)
    c_ville = models.CharField("Ville", max_length = 128)
    c_pays = models.CharField("Pays", max_length = 128)
    
    def __unicode__(self):
        return self.c_name
    def __str__(self):
        return '%s' % (self.c_name)
    
    
class ContactForm(ModelForm): #Formulaire de contact lié au model
    class Meta:
        model = Contact
        fields = ['c_name','c_nbPersonnes','c_nomsPersonnes', 'c_email','c_mdp','c_numTel','c_adresse','c_codepostal','c_ville','c_pays']

class Articles(models.Model):
    a_statut_liste=(
        ('1','1 pers'),
        ('2','2 pers'),
        ('3','3 pers'),
        ('4','4 pers'),
        ('5','5 pers'),
        ('6','6 pers'),
        ('7','7 pers'),
        ('8','8 pers'),
        ('9','9 pers'),
        
        )
    a_type_liste=(
        ('1','1 portion'),
        ('2','2 portions'),
        ('3','3 portions'),
        ('4','4 portions'),
        ('5','5 portions'),
        ('6','6 portions'),
        ('7','7 portions'),
        ('8','8 portions'),
        ('9','9 portion'),
        )
    
    # alimentaire
    a_statut=models.CharField("Nombre de personne foyer", max_length=16,choices=a_statut_liste,default='1')
    a_type=models.CharField("Portion de riz souhaitée", max_length=16,choices=a_type_liste,default='1')
    a_type2=models.CharField("Portion de pates souhaitée", max_length=16,choices=a_type_liste,default='1')
    a_type3=models.CharField("Portion de viande souhaitée", max_length=16,choices=a_type_liste,default='1')
    a_type4=models.CharField("Portion de boeuf souhaitée", max_length=16,choices=a_type_liste,default='1')
    a_type5=models.CharField("Portion de crevette souhaitée", max_length=16,choices=a_type_liste,default='1')
    a_type6=models.CharField("Nombre de gel hydroalcoolique souhaité", max_length=16,choices=a_type_liste,default='1')
    a_type7=models.CharField("Portion de Jambon souhaitée", max_length=16,choices=a_type_liste,default='1')
    a_type10=models.CharField("Nombre de bouteille de lait souhaité", max_length=16,choices=a_type_liste,default='1')
    a_type11=models.CharField("Nombre de masque souhaité", max_length=16,choices=a_type_liste,default='1')
    a_type12=models.CharField("Nombre de boite d'oeuf souhaité", max_length=16,choices=a_type_liste,default='1')
    a_type13=models.CharField("Portion de pomme de terre souhaitée", max_length=16,choices=a_type_liste,default='1')
    a_type14=models.CharField("Portion de poulet souhaitée", max_length=16,choices=a_type_liste,default='1')
    a_type15=models.CharField("Portion de tomate souhaitée", max_length=16,choices=a_type_liste,default='1')
    a_type17=models.CharField("Portion de sucre souhaitée", max_length=16,choices=a_type_liste,default='1')
    a_type18=models.CharField("Nombre de pack de farine souhaitée", max_length=10,choices=a_type_liste,default='1')
    a_type19=models.CharField("Nombre de boite de thon souhaité", max_length=10,choices=a_type_liste,default='1')
    
     # hygiène
    a_type21=models.CharField("Nombre de pack de couches pour bébé souhaité", max_length=10,choices=a_type_liste,default='1')
    a_type22=models.CharField("Nombre de tube de dentifrice souhaité", max_length=10,choices=a_type_liste,default='1')
    a_type23=models.CharField("Nombre de pack de papier toilette souhaité", max_length=10,choices=a_type_liste,default='1')
    a_type24=models.CharField("Nombre de savon pour les mains souhaité", max_length=10,choices=a_type_liste,default='1')
    a_type25=models.CharField("Nombre de tube de shampoing souhaité", max_length=10,choices=a_type_liste,default='1')
    a_description=models.TextField("un produit à suggérer")
    
    def __unicode__(self):
        return self.c_name
    def __str__(self):
        return '%s' % (self.c_name)
    
class ArticlesForm(ModelForm): #Formulaire de contact lié au model
    class Meta:
        model = Articles
        fields = ['a_statut','a_type','a_type2', 'a_type3','a_type4','a_type5','a_type6','a_type7','a_type10','a_type11','a_type12','a_type13','a_type14','a_type15','a_type17','a_type18','a_type19','a_type21','a_type22','a_type23','a_type24','a_type25','a_description']