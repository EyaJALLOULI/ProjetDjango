from django.shortcuts import render
from UserApp.models import User
from django.views.generic import ListView
from .forms import UserRegisterForm
from django.shortcuts import redirect
from django.contrib.auth import logout


# Create your views here.

class UsersListView(ListView):
    model=User
    context_object_name= 'allUsers'
    template_name= 'User/AllUsers.html'

#new
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


def logout_view(req):
    logout(req)
    return redirect("login")







    

