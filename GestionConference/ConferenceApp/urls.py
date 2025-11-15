
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
      path('Liste_Submission/<str:pk>/', views.SubmissionListView.as_view(), name='all_Submissions'),
      path('details/<str:pk>/', views.SubmissionsDetailView.as_view(), name='details'),
      path('formSubmission/',views.SubmissionCreateView .as_view(), name='Submission_add'),
      path('UpdateSubmission/<str:pk>/',views.SubmissionUpdate .as_view(), name='UpdateSubmission'),
]





