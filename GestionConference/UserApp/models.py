from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

import uuid #importation du module uuid pour la génération de  chaine de caractères aléatoires


def generate_user_id():
    return "USER"+uuid.uuid4().hex[:4].upper()

def verify_email(email):
    domaine=["esprit.tn","seasame.com","tek.tn","central.com"]
    if email.split('@')[-1] not in domaine: #split('@') donne ["eya.jallouli",esprit.tn] donc [-1] pr prendre partie aprés @ cad le drnier elm tab
        raise ValidationError("Email domain is not allowed, it must be one of private domains")  #from django.core.exceptions import ValidationError

#from django.core.validators import RegexValidator
name_validators=RegexValidator(
    regex=r'^[A-Za-z\s-]+$', #r pour raw string cad ignorer les caractères d'échappement \s pour espace et - pour tiret
    # + pour indiquer que le motif peut se répéter une ou plusieurs fois
    message='Name must contain only letters, spaces, and hyphens.'
)
      

class User(AbstractUser):
    user_id=models.CharField(max_length=8,primary_key=True,unique=True,editable=False)

    first_name=models.CharField(max_length=100,validators=[name_validators]) 
    last_name=models.CharField(max_length=100,validators=[name_validators])
    
    email=models.EmailField(unique=True,validators=[verify_email]) #validators est une liste de fonctions de validation
    affiliation=models.CharField(max_length=255)
    nationality=models.CharField(max_length=255)
    ROLE= [("participant","Participant"),("commitee","organizing comitee member")]
    role=models.CharField(max_length=255,choices= ROLE,default="participant") 

    #dans chaque modele: 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):  #fonction pour ajouter un user dans la base de données , c est la redéfinition de la méthode save 
        #args est si je ne sais pas le nombre d'arguments que je vais envoyer
        #kwargs est pour 
        if not self.user_id:
            new_id=generate_user_id()
            while User.objects.filter(user_id=new_id).exists(): #vérifier si l'id généré n'existe pas déjà dans la base de données
                new_id=generate_user_id()
            self.user_id=new_id
        super().save(*args,**kwargs) #appel de la méthode save de la classe mere (AbstractUser) pour effectuer l'enregistrement réel de l'utilisateur dans la base de données donc de tt les champs snn il va ignorer les autres champs

    #submissions=models.ManyToManyField('ConferenceApp.Conference',through='UserApp.Submission')
    #Organizer_committees=models.ManyToManyField('ConferenceApp.Conference',through='UserApp.Organizer_committee')
    

class Organizer_committee(models.Model):
    user=models.ForeignKey ('UserApp.User',on_delete=models.CASCADE,related_name='commitees')
    conference=models.ForeignKey('ConferenceApp.Conference',on_delete=models.CASCADE ,related_name='commitees')

    ROLES=[("chair","Chair"),("co-chair","Co-Chair"),("member","Member")]
    commitee_role=models.CharField(max_length=255,choices=ROLES)
    date_join=models.DateField(auto_now_add=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    

    
