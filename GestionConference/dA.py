"""

#crud User -> dans userApp
########creation d un nouveau compte

#creation fichier forms.py
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class UserRegisterForm(UserCreationForm): #on herite username password pr connecter
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2","affiliation","nationality"]
        widgets={ "email":forms.EmailInput(),
                 "password1":forms.PasswordInput()}




from .forms import UserRegisterForm
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import render
#views.py de userApp
def register(req):
    if req.method =="POST": # envoyer les info pour faire login
        #creer un formulaire personalise car on ne va pas afficher ts les champs de form comme role -> c est par defaut participant
        form=UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect("login")
    
    else: # afficher interface vide pr faire register
        form=UserRegisterForm()
    return render(req,'User/register.html',{'form':form})



# urls.py de UserAPp
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    path("login/",LoginView.as_view(template_name="login.html"),name="login"),
    path("logout/", views.logout_view , name="logout"),

]



# dans templates: User/register.html
{% extends 'base.html' %}
{% block content %}

<h2>Créer un compte participant</h2>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">S'inscrire</button>
</form>

{% endblock %}


#django connait l emplacement de register grace au fichier settings.py 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR /'GestionConference/Templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },





##############Login
#urls.py de UserApp
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [

    path("login/",LoginView.as_view(template_name="login.html"),name="login"),
    
]


#login.html
{% extends 'base.html' %}
{% block content %}

<h2>conncetion</h2>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Se connecter</button>
</form>

{% endblock %}


#setting.py
#ON A PAS personnalise la fonction donc on a pas succes url donc on modifie ici 
LOGIN_REDIRECT_URL="all_conferences"







##### il faux changer base.html
<html>
<body>
    <nav>
        <a>Home</a>
        <a href="{% url 'all_conferences' %}">Conferences</a>
        <a href="">Contact</a>
        {%if user.is_authenticated %}
        <a>{{user.username}}</a>
        <a href="{% url 'logout' %}">logout</a>
        {% else %}
        <a href="{% url 'login' %}">Login</a>
        <a href="{% url 'register' %}">Inscription</a>
        {% endif %}
    </nav>

    <div>
        {% block content %}{% endblock %}
    </div>


    <footer>
        <p>2025-2026</p>
         <p>Django</p>

    </footer>

</body>
</html>





##### logout
#views.py
from django.contrib.auth import logout
def logout_view(req):
    logout(req)
    return redirect("login")

#urls.py de userApp
urlpatterns = [
    path("logout/", views.logout_view , name="logout"),

]

#remaque on a pas de logout.html on affiche rien juste redirection vers login

### Limiter acces de qq chose a un user chose
            {% if user.is_authenticated and user.role == 'commitee' %}
                
            {% endif %}

"""""""""""


#### on ne consulte rien sauf si on a fait le login
# dans settings .py
LOGIN_URL="login"
# dans views de chaque App autre que user 
from django.contrib.auth.mixins import LoginRequiredMixin
# mettre  LoginRequiredMixin comme premier attribut de chaque fonction de views






