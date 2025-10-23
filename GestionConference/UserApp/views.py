from django.shortcuts import render
from UserApp.models import User
from django.views.generic import ListView

# Create your views here.

class UsersListView(ListView):
    model=User
    context_object_name= 'allUsers'
    template_name= 'User/AllUsers.html'