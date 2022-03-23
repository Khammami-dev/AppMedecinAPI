from django.urls import re_path as url
from PathologieApp import views

urlpatterns=[
    url(r'symptome/$',views.symptomeApi),
    url(r'symptome/([0-9]+)$',views.symptomeApi),

    url(r'pathologie/$',views.pathologieApi),
    url(r'pathologie/([0-9]+)$',views.pathologieApi),

]
