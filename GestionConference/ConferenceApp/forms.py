
from django import forms
from .models import Conference,Submission

class ConferenceFormModel(forms.ModelForm):
    #pr ajouter les chose personnalise 
    class Meta:
        model=Conference
        fields=['name','theme','description','start_date','end_date']
        labels={
            'name':'nom de la conference',      #nommer chaque champs/ syntaxe: nomchamps:nouv nom
            'theme':'theme de la conference',
            'description' :'description de la conference',
            'start_date':'date debut de la conference',
            'end_date':'date fin de la conference'
        }

        widgets={  #pr dire end date et start date de type date
            'start_date': forms.DateInput(attrs={'type':'date',}),
            'end_date': forms.DateInput(attrs={'type':'date',}),
            'name':forms.TextInput(attrs={'placeholder':'nom de la conference'})
        }




class SubmissionFormModel(forms.ModelForm):
    class Meta:
        model = Submission
        # Inclure tous les champs que l'utilisateur peut remplir
        fields = ['conference_id', 'title', 'abstract', 'keywords', 'paper', 'status', 'payed']

        # Pour changer les labels et rendre le formulaire plus lisible
        labels = {
            'conference_id': 'Conference',
            'title': 'Title',
            'abstract': 'Abstract',
            'keywords': 'Keywords',
            'paper': 'Upload Paper',
            'status': 'Submission Status',
            'payed': 'Payment Completed?',
        }

        

class SubmissionUpdateFormModel(forms.ModelForm):
    class Meta:
        model = Submission
        # Inclure tous les champs que l'utilisateur peut Modifier title, abstract, keywords, paper.
        fields = [ 'title', 'abstract', 'keywords', 'paper']

        # Pour changer les labels et rendre le formulaire plus lisible
        labels = {
            'conference_id': 'Conference',
            'title': 'Title',
            'abstract': 'Abstract',
            'keywords': 'Keywords',
            'paper': 'Upload Paper',
            
        }



        

