
from django import forms
from .models import Conference

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

