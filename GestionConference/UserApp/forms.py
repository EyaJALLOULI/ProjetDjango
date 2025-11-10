# on ne va pas utiliser conderenceModel(forms.Model)
 #model=Conference
#fields=
# car il ya password et confirm password -> on le herite de UsercreationForm

from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class UserRegisterForm(UserCreationForm): #on herite username password pr connecter
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2","affiliation","nationality"]
        widgets={ "email":forms.EmailInput(),
                 "password1":forms.PasswordInput()}


