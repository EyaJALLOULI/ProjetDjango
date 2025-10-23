from django.shortcuts import render
from django.views.generic import ListView,DetailView
from SessionApp.models import Session

# Create your views here.
class SessionListView(ListView):
    model=Session
    context_object_name='lesSessions'
    template_name='Session/detailSession.html' 

class SessioneDetailView(DetailView):
    model = Session
    context_object_name = 'detailsSessions'
    template_name = 'Session/detailForSession.html'

