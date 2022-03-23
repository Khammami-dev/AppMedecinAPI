from django.db import models

# Create your models here.

class Symptomes(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    description = models.TextField(max_length=256)


class Pathologies(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    famille = models.CharField(max_length=100)
    symptome = models.CharField(max_length=100)
    description = models.TextField(max_length=256)


