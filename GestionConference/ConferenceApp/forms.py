
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


from django import forms
from .models import Submission
from django.utils.safestring import mark_safe

class SubmissionFormModel(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['conference_id', 'title', 'abstract', 'keywords', 'paper', 'status', 'payed']
        labels = {
            'conference_id': 'Conference',
            'title': 'Title',
            'abstract': 'Abstract',
            'keywords': 'Keywords',
            'paper': 'Upload Paper',
            'status': 'Submission Status',
            'payed': 'Payment Completed?',
        }

    # Ajouter un lien de téléchargement si un fichier existe
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.paper:
            self.fields['paper'].help_text = mark_safe(
                f'<a href="{self.instance.paper.url}" download>Télécharger le fichier actuel</a>'
            )

        


class SubmissionUpdateFormModel(forms.ModelForm):
    #pr ajouter les chose personnalise 
    class Meta:
        model=Submission
        fields=['title','abstract','keywords','paper']
       