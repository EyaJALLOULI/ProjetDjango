from rest_framework.routers import DefaultRouter
from .views import SessionViewSet
from django.urls import path, include



#on ajout modification mais j ai utlise view set; il sont pret / les url aussi/ on a les PermissionError


router = DefaultRouter()
router.register('sessions',SessionViewSet)


urlpatterns = [
    path('',include (router.urls))

]