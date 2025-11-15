from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
import uuid

def generate_unique_submission_id():
     return "SUB-"+uuid.uuid4().hex[:6].upper()

def KeyWord_Validators(value):
    if len(value.split(','))>10:
        raise ValidationError("You can enter up to 10 keywords only")



paper_validators=FileExtensionValidator(allowed_extensions=['pdf'],message="Only PDF and Word documents are allowed.")


class Conference(models.Model):
    conference_id=models.AutoField(primary_key=True,unique=True,editable=False)
    name=models.CharField(max_length=255)
    description=models.TextField()
    location=models.CharField(max_length=255)
   
    THEME=[
        ("Computer Science & Artificial Intelligence","Computer Science & Artificial Intelligence"),
        ("Science & Engineering","Science & Engineering"),
        ("Social Sciences & Education","Social Sciences & Education"),
        ("Interdisciplinary Themes","Interdisciplinary Themes")
    ]
    theme=models.CharField(max_length=255,choices=THEME)
    start_date=models.DateField()
    end_date=models.DateField()

    ceated_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self): #methode pour afficher une reprsentation lisible de l'objet et ne pas l'objet lui-mme
            return f"{self.name} - {self.theme} ({self.start_date} to {self.end_date})"

class Submission(models.Model):
    submission_id=models.CharField(primary_key=True,unique=True,editable=False,max_length=255,default=generate_unique_submission_id)

    user_id=models.ForeignKey ('UserApp.User',on_delete=models.CASCADE,related_name='submissions') 
    #user_id.submissions.all()
    
    conference_id=models.ForeignKey('ConferenceApp.Conference',on_delete=models.CASCADE ,related_name='conference_submissions')

    title=models.CharField(max_length=255)
    abstract=models.TextField()
    keywords=models.TextField(validators=
                              [KeyWord_Validators]) 
    paper=models.FileField(upload_to='papers/', validators=[paper_validators]) 

    CHOICES=[
        ("submitted","Submitted"),
        ("under review","Under Review"),
        ("accepted","Accepted"),
        ("rejected","Rejected")
    ]


    status=models.CharField(max_length=255,choices=CHOICES)
    payed=models.BooleanField(default=False)
    submission_date=models.DateField(auto_now_add=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

"""
    def clean(self):
       # submission_date = timezone.now().date()
       # conference = self.conference_id 
       # if submission_date > conference.start_date:
            # raise ValidationError("Submission date must be before the conference start date.")
         
        # (En Limiter le nombre de conférences qu'un participant peut déposer une soumission  par jour (ex : 3 conférences max par jour). (En utilisant la fonction clean) 
        
        user_submissions_today = Submission.objects.filter(
            user_id=self.user_id,
            submission_date=self.submission_date
        ).count()
        if user_submissions_today >= 3:
            raise ValidationError("You can submit to a maximum of 3 conferences per day.")

 
    def save(self, *args, **kwargs):
        if not self.submission_id:
            new_id = generate_unique_submission_id()
            while Submission.objects.filter(submission_id=new_id):
                new_id = generate_unique_submission_id()
            self.submission_id = new_id
        super().save(*args, **kwargs)

        
"""
        
        
    

