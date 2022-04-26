from django.db import models

# Create your models here.

class Exercices(models.Model):
    id=models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField(max_length=256)
    critere = models.CharField(max_length=100)
    def __str__(self):
	    return self.nom
    
	

class Symptomes(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField(max_length=256)
    exercices = models.ManyToManyField(Exercices)
    def __str__(self):
	    return self.nom


class Pathologies(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)
    description = models.TextField(max_length=256)
    symptomes = models.ManyToManyField(Symptomes)
    def __str__(self):
	    return self.nom
    

class Patients(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    sexe = models.CharField(max_length=100)
    datePermis = models.CharField(max_length=100)
    autreMaladies = models.CharField(max_length=100)
    pathologie= models.ForeignKey(Pathologies, on_delete=models.CASCADE)
    def __str__(self):
	    return self.nom
    




