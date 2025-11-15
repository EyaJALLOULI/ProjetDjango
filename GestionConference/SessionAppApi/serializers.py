
from rest_framework import serializers
from SessionApp.models import Session

#rendre les donnees standards
#on import le meme modele

#fonctionalite metier dans views -> de meme ici
class sessionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Session
        fields='__all__'

