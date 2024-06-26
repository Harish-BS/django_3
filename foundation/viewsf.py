from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view 
from django.contrib.auth import authenticate, login
from rest_framework.response import Response 
from rest_framework import status 
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from .models import statuss
from .models import stage
from .serializers import statussserializer
from .serializers import stageserializer



@api_view(['GET','POST'])

def statuss_list(request):
    if request.method == 'GET':
        stat = statuss.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5
        result_page = paginator.paginate_queryset(stat, request)
        serializer = statussserializer(result_page, many = True)
        return paginator.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer = stageserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": serializer.data
            }
        return Response(response, status=status.HTTP_200_OK)
    
@api_view(['GET','POST'])

def stage_list(request):
    if request.method == 'GET':
        stag = stage.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5
        result_page = paginator.paginate_queryset(stag, request)
        serializer = stageserializer(result_page, many = True)
        return paginator.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer = stageserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": serializer.data
            }
        return Response(response, status=status.HTTP_200_OK)