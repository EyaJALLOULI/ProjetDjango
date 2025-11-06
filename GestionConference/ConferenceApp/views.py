from django.shortcuts import render
from ConferenceApp.models import Conference
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import ConferenceFormModel

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



    

class ConferenceCreate(CreateView):
    model=Conference
    template_name="Conference/conference_form.html"
    #fields="__all__" #j ai besoin de ts les fields du form sans personnalisation
    form_class=ConferenceFormModel
    success_url=reverse_lazy("all_conferences") #si succes on va consulter ts les conf / all_conferences et name de url dans urls.py




class ConferenceUpdate(UpdateView):
    model=Conference
    template_name="Conference/conference_form.html" #meme form que create
    #fields="__all__"  # cest si form par defaut
    form_class=ConferenceFormModel
    success_url=reverse_lazy("all_conferences") 

class ConferenceDelete(DeleteView):
    model=Conference
    template_name = 'Conference/conference_confirm_delete.html'
    success_url=reverse_lazy("all_conferences") 


    
    
    

    


