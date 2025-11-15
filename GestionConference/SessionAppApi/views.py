from django.shortcuts import render

# Create your views here.
 # on a deux methode -> api view ou -> viewSet
 
from rest_framework import viewsets,filters
from SessionApp.models import Session
from .serializers import sessionSerializer
from django_filters.rest_framework import DjangoFilterBackend


#sans filtre
"""
class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class=sessionSerializer
"""


# avec filtre 
class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = sessionSerializer

    # Filtres DRF
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['title']   ## matching 100%

    # 2️⃣ Recherche textuelle : partial match
    search_fields = ['topic']  


    ordering_fields = ['start_time']  

    ordering = ['session_day']  # par defaut 




# il gere ts seul les urls on les configure