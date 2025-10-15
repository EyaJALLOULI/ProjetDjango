from django.contrib import admin
from .models import User,Organizer_committee  #importation du modele User pour l enregistrer dans l interface d administration de django
# Register your models here.

admin.site.register(User)  #pour enregistrer le modele User dans l interface d administration de django
admin.site.register(Organizer_committee)