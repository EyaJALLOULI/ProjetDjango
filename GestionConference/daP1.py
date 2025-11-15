
# dans settings.py

AUTH_USER_MODEL='UserApp.User' # pr dire le user est personnalise

INSTALLED_APPS = [
    ' nomApp',
]



#######modele user userApp
#models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):

    user_id=models.CharField(max_length=8,primary_key=True,unique=True,editable=False)   #ou autofield

    first_name=models.CharField(max_length=100,validators=[name_validators]) 
    
    email=models.EmailField(unique=True,validators=[verify_email])

    ROLE= [("participant","Participant"),("commitee","organizing comitee member")]
    
    role=models.CharField(max_length=255,choices= ROLE,default="participant") 



    #dans chaque modele: 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def save(self,*args,**kwargs):
        if not self.user_id:
            new_id=generate_user_id()
            while User.objects.filter(user_id=new_id).exists(): #vérifier si l'id généré n'existe pas déjà dans la base de données
                new_id=generate_user_id()
            self.user_id=new_id
        super().save(*args,**kwargs)

    #submissions=models.ManyToManyField('ConferenceApp.Conference',through='UserApp.Submission')
    #Organizer_committees=models.ManyToManyField('ConferenceApp.Conference',through='UserApp.Organizer_committee')
    



#######les validators

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


import uuid
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
      


def KeyWord_Validators(value):
    if len(value.split(','))>10:
        raise ValidationError("You can enter up to 10 keywords only")




from django.core.validators import FileExtensionValidator
paper_validators=FileExtensionValidator(allowed_extensions=['pdf'],message="Only PDF and Word documents are allowed.")


# dans le modele luimeme
def clean(self):
       # submission_date = timezone.now().date()
       # conference = self.conference_id 
       # if submission_date > conference.start_date:
            # raise ValidationError("Submission date must be before the conference start date.")
         
        # (En Limiter le nombre de conférences qu'un participant peut déposer une soumission  par jour (ex : 3 conférences max par jour). (En utilisant la fonction clean) 
        
        user_submissions_today = Submission.objects.filter(
            user_id=self.user_id,
            submission_date=self.submission_date
        ).count()
        if user_submissions_today >= 3:
            raise ValidationError("You can submit to a maximum of 3 conferences per day.")
#self.user_id: l’utilisateur de la submission que tu es en train de créer
#user_id : colonne user_id


def clean(self):
        if self.session_day < self.conference.start_date or self.session_day > self.conference.end_date:
            raise ValidationError("Session date must be within the conference dates.")
        
        if self.start_time >= self.end_time:
            raise ValidationError("Session start time must be before end time.")

        






# gestion des fk; ou les mettre?
'''
Pour une relation Many-to-One ou One-to-One : instance.foreignkey.champ → accès à la valeur du champ de l’objet lié

Pour une relation Many-to-Many ou inverse : instance.many_related.all() ou .filter(...) → liste des objets liés '''
##################################Many to many
#################################3#############avec classe d'association   /les deux autres classes  sont normal


class Submission(models.Model):
    submission_id=models.CharField(primary_key=True,unique=True,editable=False,max_length=255,default=generate_unique_submission_id)

    user_id=models.ForeignKey ('UserApp.User',on_delete=models.CASCADE,related_name='submissions') 
    #user_id.submissions.all()
    
    conference_id=models.ForeignKey('ConferenceApp.Conference',on_delete=models.CASCADE ,related_name='conference_submissions')



######################### sans  classe d'association   many to many
class Publications(models.Model):
    title = models.CharField(max_length=30) 
 

class Articles(models.Model):
    headline = models.CharField(max_length=100) 
    publications = models.ManyToManyField(Publications)



#################many to one
class Reporter(models.Model): #one parent
    first_name = models.CharField(max_length=30) 

class Articles(models.Model): # apres de many 
    reporter = models.ForeignKey(Reporter,on_delete = models.CASCADE,)


#Models.PROTECT: empêche la suppression du parent si les enfants existent.
 #=> Un ProtectedError est levé si on tente de supprimer un Reporter ayant des Articles.

#• Models.RESTRICT: similaire à PROTECT mais plus flexible. Une logique 
#personnalisée peut être défini.
 #=> Un RestrictedError si des Articles existent.

#• Models.SET_NULL: met la clé étrangère à NULL.
# => Les Articles restent mais reporter devient NULL.


#Models.SET_DEFAULT: assigne la valeur par défaut du champ. L'option default=… 
#est obligatoire.
# => La valeur de l'ID = 9999 est affectée.

"""
get_deleted_reporter():   # remplace par un autre reporter qui a un champs name = unknown reporter
    return Reporter.objects.get(name="Unkown Reporter") 

class Article(models.Model):
    reporter = models.ForeignKey(Reporter, on_delete = models.SET(get_deleted_reporter), )
"""



##########One to one
class Place(models.Model):
    name = models.CharField(max_length=50) 
    address = models.CharField(max_length=80)

class Restaurant(models.Model):
    place = models.OneToOneField( Place,on_delete = models.CASCADE, primary_key = True,)   #oui pr les deux classes/ selon la logique


def __str__(self): #methode pour afficher une reprsentation lisible de l'objet et ne pas l'objet lui-mme
            return f"{self.name} - {self.theme} ({self.start_date} to {self.end_date})"
