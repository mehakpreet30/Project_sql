import imp
from math import fabs
from urllib import response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from accounts.models import Staff
from accounts.serializers import StaffSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

# Create your views here.



@csrf_exempt
def staffAPI(request, id=0):
    if request.method=='GET':
        staff= Staff.objects.all()
        staff_serializer= StaffSerializer(staff, many= True)
        return JsonResponse(staff_serializer.data, safe=False)   

@csrf_exempt
def createStaff(request, id=0):
     if request.method=='POST':
            staff_data= JSONParser().parse(request)
            staff_serializer = StaffSerializer(data= staff_data)
            if staff_serializer.is_valid():
                staff_serializer.save()
                return JsonResponse("Add successfully", safe=False)
            return JsonResponse("Failed to add", safe= False)


@csrf_exempt
def updateStaff(request, id=0):
    if request.method=='PUT':
        staff_data= JSONParser().parse(request)
        staff= Staff.objects.get(departmentId=staff_data['departmentId'])
        staff_serializer = StaffSerializer(staff,data= staff_data)
        if staff_serializer.is_valid():
            staff_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe= False)


@csrf_exempt
def deleteStaff(request, id=0):
    if request.method=='DELETE':
        staff= Staff.objects.get(departmentId=id)
        staff.delete()
        return JsonResponse("Deleted Sucessfully", safe= False)









    

