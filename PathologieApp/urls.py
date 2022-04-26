from django.urls import re_path as url
from PathologieApp import views

urlpatterns=[
    url(r'symptome/$',views.symptomeApi),
    url(r'symptome/([0-9]+)$',views.symptomeApi),

    url(r'pathologie/$',views.pathologieApi),
    url(r'pathologie/([0-9]+)$',views.pathologieApi),

    url(r'exercice/$',views.exerciceApi),
    url(r'exercice/([0-9]+)$',views.exerciceApi),

    url(r'patient/$',views.patientApi),
    url(r'pathologie/([0-9]+)$',views.patientApi),

]
