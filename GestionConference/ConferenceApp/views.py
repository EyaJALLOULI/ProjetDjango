from django.shortcuts import render
from ConferenceApp.models import Conference, Submission
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import ConferenceFormModel,SubmissionFormModel,SubmissionUpdateFormModel
from django.contrib.auth.mixins import LoginRequiredMixin


#function based
def all_conferences(request):
    conferences = Conference.objects.all()
    return render(request, 'Conference\liste.html', {'Liste_conferences': conferences})
    
#class based
class conferenceListView( LoginRequiredMixin,ListView):
    model = Conference
    context_object_name = 'Liste_conferences'
    ordering = ['start_date']
    template_name = 'Conference/liste.html'


class conferenceDetailView(LoginRequiredMixin,DetailView):
    model = Conference
    context_object_name = 'dconference'
    template_name = 'Conference/details.html'



    

class ConferenceCreate( LoginRequiredMixin,CreateView):
    model=Conference
    template_name="Conference/conference_form.html"
    #fields="__all__" #j ai besoin de ts les fields du form sans personnalisation
    form_class=ConferenceFormModel
    success_url=reverse_lazy("all_conferences") #si succes on va consulter ts les conf / all_conferences et name de url dans urls.py




class ConferenceUpdate( LoginRequiredMixin,UpdateView):
    model=Conference
    template_name="Conference/conference_form.html" #meme form que create
    #fields="__all__"  # cest si form par defaut
    form_class=ConferenceFormModel
    success_url=reverse_lazy("all_conferences") 

class ConferenceDelete( LoginRequiredMixin,DeleteView):
    model=Conference
    template_name = 'Conference/conference_confirm_delete.html'
    success_url=reverse_lazy("all_conferences") 



"""

class SubmissionListView( LoginRequiredMixin,ListView):
    model = Submission
    context_object_name = 'Liste_Submission'
    template_name = 'Submission/liste.html'

    def get_queryset(self):
        id = self.kwargs['pk']
        return Submission.objects.filter(conference_id=id)
    


class SubmissionDetailView(LoginRequiredMixin,DetailView):
    model = Submission
    context_object_name = 'dSubmission'
    template_name = 'Submission/details.html'


from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Submission
from .forms import SubmissionFormModel

class SubmissionCreateView(LoginRequiredMixin, CreateView):
    model = Submission
    template_name = "Submission/Submission_form.html"
    form_class = SubmissionFormModel
    success_url = reverse_lazy("all_Submission")

class SubmissionCreateView(LoginRequiredMixin, CreateView):
    model = Submission
    template_name = "Submission/Submission_form.html"
    form_class = SubmissionFormModel
    success_url = reverse_lazy("all_Submission")

    def form_valid(self, form):
        # Assigner l'utilisateur connecté au bon champ
        form.instance.user_id_id = self.request.user
        print("Usekkkr:", self.request.user)

        return super().form_valid(form)
        
 

    
class SubmissionUpdate( LoginRequiredMixin,UpdateView):
    model=Submission
    template_name="Submission/Submission_form.html" #meme form que create
    #fields="__all__"  # cest si form par defaut
    #title, abstract, keywords, paper.
    form_class= SubmissionUpdateFormModel
    success_url=reverse_lazy("all_Submission") 

     

"""



class SubmissionListView( LoginRequiredMixin,ListView):
    model = Submission
    context_object_name = 'Liste_Submission'
   
    template_name = 'Submissions/liste.html'

    #on peut ne pas afficher tte la liste en faisant filtrage avec 
    def get_queryset(self):
        id = self.kwargs['pk']

        return Submission.objects.filter(
            conference_id=id,
            user_id=self.request.user.pk
        )

class SubmissionsDetailView(LoginRequiredMixin,DetailView):
    model = Submission
    context_object_name = 'sub'
    template_name = 'Submissions/details.html'

from django.urls import path
class SubmissionCreateView( LoginRequiredMixin,CreateView):
    model=Submission
    template_name="Submissions/Submissions_form.html"
    
    form_class=SubmissionFormModel 
    
    
    
    def get_success_url(self):
        return reverse_lazy('all_Submissions', kwargs={'pk': self.object.conference_id_id})

    def form_valid(self, form):
        form.instance.user_id_id = self.request.user.pk
        return super().form_valid(form)





""" (Une soumission avec l’état accepté ou rejeté ne peut pas être modifiable) 
b. 
Les champs modifiables sont : title, abstract, keywords, paper. 
c. 
Les champs non modifiables : submission_id, submission_date, user. 

"""

class SubmissionUpdate( LoginRequiredMixin,UpdateView):
    model=Submission
    template_name="Submissions/Submissions_form.html"
    form_class=SubmissionUpdateFormModel
    def get_success_url(self):
        return reverse_lazy('all_Submissions', kwargs={'pk': self.object.conference_id_id})


          