"""
#crud modele normal -> pas dans admin -> on travail dans front

#dans views.py
#class based

#affichage des conferences:
from ConferenceApp.models import Conference
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class conferenceListView( LoginRequiredMixin,ListView):
    model = Conference
    context_object_name = 'Liste_conferences'
    ordering = ['start_date']
    template_name = 'Conference/liste.html'

    #on peut ne pas afficher tte la liste en faisant filtrage avec 
    def get_queryset(self):
        id = self.kwargs['pk']
        return Submission.objects.filter(conference_id=id) #filtre la liste selon le pk de la conférence passé dans l’URL



####dans templates, Conference/liste.html:
{% extends "base.html" %}

{% block content %}
<h2>Liste des conférences</h2>


<table border="1">
    <tr>
        <td>Titre</td>
        <td>Locationn</td>
        <td>action</td>
    </tr>

    {% for c in Liste_conferences %}
        <tr>
            <td>{{ c.name }}</td>
            <td>{{ c.location }}</td>
        </tr>
    {% endfor %}
</table>
{% endblock %}


#dans urls.py de modele a afficher

from django.urls import path
#from .views import *
from . import views

urlpatterns = [
    path('Liste_conferences/', views.conferenceListView.as_view(), name='all_conferences'),
]



##########afficher detail d une seul instance selon leur pk
#dans liste.html de ts les conference affichee
 <td><a href="{% url 'conference_detail' c.pk %}">Voir Détails</a></td>
#c de boucle for
 


##dans views de modele a afficher
from ConferenceApp.models import Conference
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class conferenceDetailView(LoginRequiredMixin,DetailView):
    model = Conference
    context_object_name = 'dconference'
    template_name = 'Conference/details.html'



####dans templates, Conference/details.html:
{% extends "base.html" %}

{% block content %}
<h1>{{dconference.name}}</h1>
{% endblock %}


#dans urls.py de modele a afficher

from django.urls import path
#from .views import *
from . import views

urlpatterns = [
    path('details/<int:pk>/', views.conferenceDetailView.as_view(), name='conference_detail'),   #<str:pk>
]





########## creation de nouvelle instance -> affichage formulaire
from ConferenceApp.models import Conference
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ConferenceFormModel
class ConferenceCreate( LoginRequiredMixin,CreateView):
    model=Conference
    template_name="Conference/conference_form.html"
    #fields="__all__" #j ai besoin de ts les fields du form sans personnalisation
    form_class=ConferenceFormModel #from .forms import ConferenceFormModel
    success_url=reverse_lazy("all_conferences") #si succes on va consulter ts les conf / all_conferences et name de url dans urls.py





#on fait la creation dans l app forms.py 

from django import forms
from .models import Conference

class ConferenceFormModel(forms.ModelForm):
    #pr ajouter les chose personnalise 
    class Meta:
        model=Conference
        fields=['name','theme','description','start_date','end_date']
        labels={
            'name':'nom de la conference',      #nommer chaque champs/ syntaxe: nomchamps:nouv nom
            'theme':'theme de la conference',
            'description' :'description de la conference',
            'start_date':'date debut de la conference',
            'end_date':'date fin de la conference'
        }

        widgets={  #pr dire end date et start date de type date
            'start_date': forms.DateInput(attrs={'type':'date',}),
            'end_date': forms.DateInput(attrs={'type':'date',}),
            'name':forms.TextInput(attrs={'placeholder':'nom de la conference'})
        }


# dans templates/Conference/conference_form.html:
{% extends "base.html" %}

{% block content %}

{% if view.object.pk %} <!--si modification on envoi un pk -> c est update  --> 
<h2>Modifier une conference</h2>
{% else %}
<h2>Ajouter une conference</h2>
{% endif %}

 
<form method="post"> 
    {% csrf_token %}   <!--token pour garentir la securite pr chaque form c est obligatoire -->
    {{form.as_p}}   <!-- form est une variable par defaut envoye par CreateView -->
    <button type="submit">Enregistrer</button>
</form>


{% endblock %}


#dans url.py de l application:

from django.urls import path
#from .views import *
from . import views

urlpatterns = [
   
    path('form/',views.ConferenceCreate.as_view(), name='conference_add'),

]





####Update 
class ConferenceUpdate( LoginRequiredMixin,UpdateView):
    model=Conference
    template_name="Conference/conference_form.html" #meme form que create
    #fields="__all__"  # cest si form par defaut
    form_class=ConferenceFormModel
    success_url=reverse_lazy("all_conferences") 

##### dans forms.py
#le meme que create

### meme html
path('<int:pk>/update/', views.ConferenceUpdate.as_view(), name='conference_Update'),

#dans la liste des conf:
 {% if user.is_authenticated and user.role == 'commitee' %}

                <td><a href="{% url 'conference_Update' c.pk %}">Modifier</a></td>
                
{% endif %}




####################"" conference delete

#####dans views.py
class ConferenceDelete( LoginRequiredMixin,DeleteView):
    model=Conference
    template_name = 'Conference/conference_confirm_delete.html'
    success_url=reverse_lazy("all_conferences") 


#Conference/conference_confirm_delete.html
{% extends "projet.html" %}

{% block content %}
    <p>Voulez-vous supprimer la conférence <strong>{{ object.name }}</strong> ?</p>

    <form method="post">
        {% csrf_token %}
        <button type="submit">Oui</button>
        <a href="{% url 'all_conferences' %}">Non</a>
    </form>
{% endblock %}



### dans url
    path('<int:pk>/delete/', views.ConferenceDelete.as_view(), name='conference_delete'),


#dans la liste des conf:
 {% if user.is_authenticated and user.role == 'commitee' %}
                <td><a href="{% url 'conference_delete' c.pk %}">Supprimer</a></td>
                
{% endif %}




"""





