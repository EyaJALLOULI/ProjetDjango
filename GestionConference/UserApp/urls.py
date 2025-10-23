from django.urls import path
#from .views import *
from . import views


urlpatterns=[
    path('AllUsers/', views.UsersListView.as_view() , name='AllUsers'),

]