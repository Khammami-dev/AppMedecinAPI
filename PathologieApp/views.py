from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  JSONParser
from PathologieApp.models import Symptomes,Pathologies
from PathologieApp.serializers import SymptomeSerializer, PathologieSerializer
from django.http.response  import JsonResponse
# Create your views here.
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




