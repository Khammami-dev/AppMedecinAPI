from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  JSONParser
from PathologieApp.models import Symptomes,Pathologies,Patients,Exercices
from PathologieApp.serializers import SymptomeSerializer, PathologieSerializer, PatientSerializer, ExerciceSerializer
from django.http.response  import JsonResponse
# Create your views here.

@csrf_exempt
def exerciceApi(request,id=0):
    if request.method=='GET':
        exercices = Exercices.objects.all()
        exercice_serializer = ExerciceSerializer(exercices, many=True)
        return JsonResponse(exercice_serializer.data, safe=False)
    elif request.method=='POST':
        exercice_data = JSONParser().parse(request)
        exercice_serializer = ExerciceSerializer(data=exercice_data)
        if exercice_serializer.is_valid():
            exercice_serializer.save()
            return JsonResponse("Added Succesfully!", safe=False)
        return JsonResponse("Faield to Add.", safe=False)
    elif request.method=='PUT':
        exercice_data= JSONParser().parse(request)
        exercice=Exercices.objects.get(id=exercice_data['id'])
        exercice_serializer=ExerciceSerializer(exercice,data=exercice_data)
        if exercice_serializer.is_valid():
            exercice_serializer.save()
            return JsonResponse("updated Successfully!!", safe=False)
        return JsonResponse("failed to update.", safe=False)
    elif request.method=='DELETE':
        exercice=Exercices.objects.get(id=id)
        exercice.delete()
        return JsonResponse("Deleted Succefully", safe=False)

@csrf_exempt
def symptomeApi(request,id=0):
    if request.method=='GET':
        symptomes = Symptomes.objects.all()
        symptome_serializer = SymptomeSerializer(symptomes, many=True)
        return JsonResponse(symptome_serializer.data, safe=False)
    elif request.method=='POST':
        symptome_data=JSONParser().parse(request)
        symptome_serializer=SymptomeSerializer(data=symptome_data)
        if symptome_serializer.is_valid():
            symptome_serializer.save()
            return JsonResponse("Added Succesfully!", safe=False)
        return JsonResponse("Faield to Add.", safe=False)
    elif request.method=='PUT':
        symptome_data= JSONParser().parse(request)
        symptome=Symptomes.objects.get(id=symptome_data['id'])
        symptome_serializer=SymptomeSerializer(symptome,data=symptome_data)
        if symptome_serializer.is_valid():
            symptome_serializer.save()
            return JsonResponse("updated Successfully!!", safe=False)
        return JsonResponse("failed to update.", safe=False)
    elif request.method=='DELETE':
        symptome=Symptomes.objects.get(id=id)
        symptome.delete()
        return JsonResponse("Deleted Succefully", safe=False)

@csrf_exempt
def pathologieApi(request,id=0):
    if request.method=='GET':
        pathologies = Pathologies.objects.all()
        pathologie_serializer = PathologieSerializer(pathologies, many=True)
        return JsonResponse(pathologie_serializer.data, safe=False)
    elif request.method=='POST':
        pathologie_data=JSONParser().parse(request)
        pathologie_serializer=PathologieSerializer(data=pathologie_data)
        if pathologie_serializer.is_valid():
            pathologie_serializer.save()
            return JsonResponse("Added Succesfully!", safe=False)
        return JsonResponse("Faield to Add.", safe=False)
    elif request.method=='PUT':
        pathologie_data= JSONParser().parse(request)
        pathologie=Pathologies.objects.get(id=pathologie_data['id'])
        pathologie_serializer=PathologieSerializer(pathologie,data=pathologie_data)
        if pathologie_serializer.is_valid():
            pathologie_serializer.save()
            return JsonResponse("updated Successfully!!", safe=False)
        return JsonResponse("failed to update.", safe=False)
    elif request.method=='DELETE':
        pathologie=Pathologies.objects.get(id=id)
        pathologie.delete()
        return JsonResponse("Deleted Succefully", safe=False)

@csrf_exempt
def patientApi(request,id=0):
    if request.method=='GET':
        patients = Patients.objects.all()
        patient_serializer = PatientSerializer(patients, many=True)
        return JsonResponse(patient_serializer.data, safe=False)
    elif request.method=='POST':
        patient_data=JSONParser().parse(request)
        patient_serializer= PatientSerializer(data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse("Added Succesfully!", safe=False)
        return JsonResponse("Faield to Add.", safe=False)
    elif request.method=='PUT':
        patient_data= JSONParser().parse(request)
        patient=Patients.objects.get(id=patient_data['id'])
        patient_serializer=PatientSerializer(patient,data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse("updated Successfully!!", safe=False)
        return JsonResponse("failed to update.", safe=False)
    elif request.method=='DELETE':
        patient=Patients.objects.get(id=id)
        patient.delete()
        return JsonResponse("Deleted Succefully", safe=False)






