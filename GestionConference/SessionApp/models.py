from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.

room_validators=RegexValidator(
    regex=r'^[A-Za-z1-9]+$', 
    message='Name must contain only letters and numbers.'
)

class Session(models.Model):
    session_id=models.AutoField(primary_key=True,unique=True,editable=False)
    title=models.CharField(max_length=255)
    topic=models.CharField(max_length=255)
    session_day=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    room=models.CharField(max_length=255 , validators=[room_validators])


    def clean(self):
        if self.session_day < self.conference.start_date or self.session_day > self.conference.end_date:
            raise ValidationError("Session date must be within the conference dates.")
        
        if self.start_time >= self.end_time:
            raise ValidationError("Session start time must be before end time.")

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    conference=models.ForeignKey('ConferenceApp.Conference',on_delete=models.CASCADE,related_name='sessions') #related_name='sessions' permet d'acceder aux sessions d'une conference via conference.sessions.all()

    #(nomApp.nomModele,...)
    # ou bien conference=models.ForeignKey(Conference)
    # donc on ajoute from ConferenceApp.models import Conference (from application fichier model import le model)



