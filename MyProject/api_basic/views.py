from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import Detail
from django.http import JsonResponse
from .serializers import DetailSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : "/detail-list/",
        'Person View' : "/person-detail/<str:pk>/",
        'Create' : "/person-create/",
        'Update' : "/person-update/<str : pk>",
        'Delete' : "/person-delete/<str : pk>",
    }
    return Response(api_urls)

@api_view(['GET'])
def detailList(request):
    details = Detail.objects.all()
    serializer = DetailSerializer(details,many = True)
    return Response(serializer.data)    

@api_view(['GET'])
def personDetail(request,pk):
    detail = Detail.objects.get(id = pk)
    serializer = DetailSerializer(detail,many = False)
    return Response(serializer.data)


@api_view(['POST'])
def createPerson(request):
    serializer = DetailSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updatePerson(request,pk):
    detail = Detail.objects.get(id = pk)
    serializer = DetailSerializer(instance = detail,data = request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_200_OK)
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletePerson(request,pk):
    detail = Detail.objects.get(id = pk)
    detail.delete()
    return Response("Record deleted Successfully")


