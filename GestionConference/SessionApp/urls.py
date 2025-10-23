from django.urls import path
from . import views

urlpatterns = [
    path('lesSessions/', views.SessionListView.as_view(), name='lesSessions'),
    path('DetailSession/<int:pk>/', views.SessioneDetailView.as_view(), name='Sessiondetail')
]