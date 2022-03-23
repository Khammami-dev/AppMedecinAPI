from rest_framework import serializers
from PathologieApp.models import Symptomes
from PathologieApp.models import Pathologies

class SymptomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptomes
        fields = ['id', 'titre', 'description']


class PathologieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pathologies
        fields = ['id', 'nom','famille','symptome','description']
