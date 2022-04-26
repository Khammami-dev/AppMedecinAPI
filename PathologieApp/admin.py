from django.contrib import admin
from PathologieApp.models import Symptomes,Pathologies,Exercices,Patients

# Register your models here.
admin.site.register(Symptomes)
admin.site.register(Pathologies)
admin.site.register(Exercices)
admin.site.register(Patients)
