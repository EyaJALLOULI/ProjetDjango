from django.shortcuts import render
from ConferenceApp.models import Conference
from django.views.generic import ListView, DetailView 

#function based
def all_conferences(request):
    conferences = Conference.objects.all()
    return render(request, 'Conference\liste.html', {'Liste_conferences': conferences})
    
#class based
class conferenceListView(ListView):
    model = Conference
    context_object_name = 'Liste_conferences'
    ordering = ['start_date']
    template_name = 'Conference/liste.html'

class conferenceDetailView(DetailView):
    model = Conference
    context_object_name = 'dconference'
    template_name = 'Conference/details.html'