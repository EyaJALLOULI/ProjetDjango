
from django.urls import path
#from .views import *
from . import views

urlpatterns = [
   #path('Liste_conferences/', views.all_conferences, name='all_conferences'),
    path('Liste_conferences/', views.conferenceListView.as_view(), name='all_conferences'),
    path('details/<int:pk>/', views.conferenceDetailView.as_view(), name='conference_detail'),

    path('form/',views.ConferenceCreate.as_view(), name='conference_add'),

    
    path('<int:pk>/update/', views.ConferenceUpdate.as_view(), name='conference_Update'),

    
    path('<int:pk>/delete/', views.ConferenceDelete.as_view(), name='conference_delete'),

    path('Liste_Submission/<int:pk>', views.SubmissionListView.as_view(), name='all_Submission'),

    path('details_submission/<str:pk>', views.SubmissionDetailView.as_view(), name='submission_detail'),

     path('form-Submission/',views.SubmissionCreateView.as_view(), name='Submission_add'),

     path('<str:pk>/update', views.SubmissionUpdate.as_view(), name='Submission_Update'),

]