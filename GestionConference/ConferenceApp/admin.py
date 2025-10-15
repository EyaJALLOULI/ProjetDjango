from django.contrib import admin
from .models import Conference
from .models import Submission

class SubmissionStackedInline(admin.StackedInline):
    model = Submission
    extra = 1 #nombre de formulaires vides supplementaires pour ajouter de nouvelles submissions
    readonly_fields = ('submission_id', 'submission_date', 'created_at', 'updated_at')
    #on peut fieldsets pour organiser les champs en sections


class SubmissionTabularInLine(admin.TabularInline):
    model = Submission
    extra = 1
    fields = ('title', 'status', 'user_id', 'payed')  
    readonly_fields = ('submission_id', 'submission_date', 'created_at', 'updated_at')

    

# Ajout: version tabulaire (affiche uniquement les champs principaux en tableau)
class SubmissionTabularInline(admin.TabularInline):
    model = Submission
    fields = ('title', 'status', 'user_id', 'payed')  # user_id = FK vers User
    extra = 0
    readonly_fields = ('submission_id', 'submission_date')  # facultatif




#admin.site.register(Conference) 
@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'theme', 'start_date', 'end_date', 'location', 'duration') 

    ordering = ('start_date',)
    list_filter = ('theme','location', 'start_date')
    search_fields = ('name', 'location', 'description') 



    fieldsets = (
        ('Information generale', {'fields': ('conference_id','name','description', 'theme')}),
        ('Dates', {'fields': ('start_date', 'end_date','location')}),
    )
    readonly_fields = ('conference_id',)

   
    date_hierarchy = 'start_date'  #ajoute une hierarchie de date en haut de la page de liste des conferences


    inlines = [SubmissionStackedInline, SubmissionTabularInLine ]  #ajoute les submissions liees a une conference dans la page de detail de la conference


    def duration(self, objet):
        if objet.start_date and objet.end_date:
             return (objet.end_date - objet.start_date).days
        return "rien a signaler"
    duration.short_description = 'Duration (days)'



admin.site.site_header = "Conference Management Admin 25/06/2025"
admin.site.site_title = "Conference Management Admin Portal"
admin.site.index_title = "Welcome to Conference Management Admin Portal"


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'user_id', 'conference_id', 'payed', 'submission_date', 'short_abstract')

    list_filter = ('status', 'payed', 'conference_id', 'submission_date')
    search_fields = ('title', 'keywords', 'user_id__username')

    list_editable = ('status', 'payed')  #permet de modifier ces champs directement depuis la liste

    fieldsets =( 
        ('Information generale', {'fields': ('submission_id', 'title', 'abstract', 'keywords')}),
        ('Fichier et conférence :', {'fields': ('paper', 'conference_id')}),
        (' Suivi:', {'fields': ('status', 'payed', 'user_id', 'submission_date')}),
    )
    readonly_fields = ('submission_id','submission_date',)


    def short_abstract(self, obj):
        if len(obj.abstract) > 50:
            return obj.abstract[:50]
        return obj.abstract
    short_abstract.short_description = 'Abstract' 


       
    
    
   