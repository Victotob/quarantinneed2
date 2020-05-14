from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms import ModelForm

# Create your models here.



class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,nbPersonnes,nomsPersonnes,numTel,adresse,codepostal,ville,pays,password=None):
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have an username")
        if not nbPersonnes:
            raise ValueError("Must enter nbPersonnes")
        if not nomsPersonnes:
            raise ValueError("Must enter nomsPersonnes")
        if not numTel:
            raise ValueError("Must enter numTel")
            
        user = self.model(
                email=self.normalize_email(email),
                username=username,
                nbPersonnes=nbPersonnes,
                nomsPersonnes=nomsPersonnes,
                numTel=numTel,      
                adresse=adresse,
                codepostal=codepostal,
                ville=ville,
                pays=pays,
                )

        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self,email,username,nbPersonnes,nomsPersonnes,numTel,adresse,codepostal,ville,pays,password):
        
        user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,  
                nbPersonnes=nbPersonnes,
                nomsPersonnes=nomsPersonnes,
                numTel=numTel,
                adresse=adresse,
                codepostal=codepostal,
                ville=ville,
                pays=pays,
                )


        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        
        user.save(using=self._db)
        
        return user





class Account(AbstractBaseUser):
    
    #Pour connection
    email = models.EmailField(verbose_name="email", max_length=60,unique=True)
    
    #Attributs demandés
    nbPersonnes=    models.IntegerField("Nombre de personnes")
    nomsPersonnes=  models.CharField("Noms des personnes", max_length = 128)
    numTel =        models.CharField("Numéro de téléphone", max_length = 128)
    adresse =       models.CharField("Adresse", max_length = 128)
    codepostal =    models.CharField("Code postal", max_length = 128)
    ville =         models.CharField("Ville", max_length = 128)
    pays =          models.CharField("Pays", max_length = 128)
       
    
    #obligatoire
    username = models.CharField(max_length = 30, unique=True)
    date_joined=models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login=models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','nbPersonnes','nomsPersonnes','numTel','adresse','codepostal','ville','pays']
    
    
    objects=MyAccountManager()
    
    def __str__(self):
        return self.email + ", " +self.username
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True
    


