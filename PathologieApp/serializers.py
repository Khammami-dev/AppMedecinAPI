from rest_framework import serializers
from PathologieApp.models import Symptomes
from PathologieApp.models import Pathologies
from PathologieApp.models import Exercices
from PathologieApp.models import Patients

class SymptomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptomes
        fields = ['id', 'nom', 'description','exercices']


class PathologieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pathologies
        fields = ['id', 'nom','categorie','description','symptomes']

class ExerciceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercices
        fields = ['id', 'nom','description','critere']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['id', 'nom','prenom','age','sexe','datePermis','autreMaladies','pathologie']                
