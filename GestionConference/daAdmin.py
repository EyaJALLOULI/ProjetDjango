#python manage.py createsuperuser

#methode 1
from .models import nomClass

#Product.tags.through 
# c est la table intermediaire


class SubmissionStackedInline(admin.StackedInline):
    model = Submission
    extra = 1
    readonly_fields = ('submission_id', 'submission_date', 'created_at', 'updated_at')
    #on peut fieldsets pour organiser les champs en sections


class SubmissionTabularInLine(admin.TabularInline):
    model = Submission
    extra = 1
    fields = ('title', 'status', 'user_id', 'payed')  
    readonly_fields = ('submission_id', 'submission_date', 'created_at', 'updated_at')


admin.site.register(nomClass)

#ou bien
@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name') 

    list_filter = ('category')

    search_fields = ('title')

    list_editable = ('price', 'stock')

    # champs cliquables pr modifier
    list_display_links = ('title')

    list_per_page = 2

    date_hierarchy = 'created'
    

    readonly_fields = ('created', 'updated') 

    exclude = ('description',) 

    #ordre des champs dans le formulaire.
    fields = ('title', 'category')

    #Organise les champs en section
    fieldsets = (
            ('Timestamps', {
            'fields': ('created', 'updated'), 
            }),
        )
    
    # Remplit automatiquement le champ slug en fonction du titre
    prepopulated_fields = {'slug': ('title',)}
                           

    # taper quelques lettres et obtenir des suggestions.
    autocomplete_fields =('category',) 



    inlines = [SubmissionStackedInline, SubmissionTabularInLine ]  #ajoute les submissions liees a une conference dans la page de detail de la conference


########################Action sur plusieurs section
        #queryset = fonction update
    @admin.action(description='Mark selected submissions as payed')
    def makrk_as_payed(modeladmin, request, queryset):
        queryset.update(payed=True)

 
    @admin.action
    def mark_as_accepted(modeladmin, request, queryset):
        queryset.update(status='accepted')

    
    actions=['makrk_as_payed', 'mark_as_accepted'] 

    # crrer un nouv champs a partir des champs existante 
    def duration(self, objet): #objet = l’instance du modèle sur laquelle tu travailles.
        if objet.start_date and objet.end_date:
             return (objet.end_date - objet.start_date).days
        return "rien a signaler"
    duration.short_description = 'Duration (days)'

    # on met duration dans liste dispaly



    



admin.site.site_header = "Conference Management Admin 25/06/2025"
admin.site.site_title = "Conference Management Admin Portal"
admin.site.index_title = "Welcome to Conference Management Admin Portal"







































    





    








@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    def short_abstract(self, obj):
        if len(obj.abstract) > 50:
            return obj.abstract[:50]
        return obj.abstract
    short_abstract.short_description = 'Abstract'



        

       
    
    
   







