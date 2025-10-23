
from django.urls import path
#from .views import *
from . import views

urlpatterns = [
   #path('Liste_conferences/', views.all_conferences, name='all_conferences'),
    path('Liste_conferences/', views.conferenceListView.as_view(), name='all_conferences'),
    path('details/<int:pk>/', views.conferenceDetailView.as_view(), name='conference_detail'),
]