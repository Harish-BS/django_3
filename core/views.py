from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view 
from django.contrib.auth import authenticate, login
from rest_framework.response import Response 
from rest_framework import status 
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from .models import project
from .models import solution
from .models import feature
from .models import task
from .serializers import projectserializer
from .serializers import solutionserializer
from .serializers import featureserializer
from .serializers import taskserializer
from .serializers import task_filterserializer


@api_view(['GET','POST'])

def project_list(request):
    if request.method == 'GET':
        pro = project.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5
        result_page = paginator.paginate_queryset(pro, request)
        serializer = projectserializer(result_page, many = True)
        return paginator.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer = projectserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": serializer.data
            }
        return Response(response, status=status.HTTP_200_OK)
        

    
@api_view(['GET','PUT','DELETE'])

def project_detail(request,id):
    try:
        emp = project.objects.get(pk=id)
    except project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = projectserializer(emp)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        serializer = projectserializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##################################################################################################################


@api_view(['GET','POST'])

def solution_list(request):
    if request.method == 'GET':
        sol = solution.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5
        result_page = paginator.paginate_queryset(sol, request)
        serializer = solutionserializer(result_page, many = True)
        return paginator.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer = solutionserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": serializer.data
            }
        return Response(response, status=status.HTTP_200_OK)
        

    
@api_view(['GET','PUT','DELETE'])

def solution_detail(request,id):
    try:
        emp = solution.objects.get(pk=id)
    except solution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = solutionserializer(emp)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        serializer = solutionserializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################################################################################################################   

@api_view(['GET','POST'])

def feature_list(request):
    if request.method == 'GET':
        feat = feature.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5
        result_page = paginator.paginate_queryset(feat, request)
        serializer = featureserializer(result_page, many = True)
        return paginator.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer = featureserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": serializer.data
            }
        return Response(response, status=status.HTTP_200_OK)
        

    
@api_view(['GET','PUT','DELETE'])

def feature_detail(request,id):
    try:
        emp = feature.objects.get(pk=id)
    except feature.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = featureserializer(emp)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        serializer = featureserializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#################################################################################################################


@api_view(['GET','POST'])

def task_list(request):
    if request.method == 'GET':
        tas = task.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5
        result_page = paginator.paginate_queryset(tas, request)
        serializer = taskserializer(result_page, many = True)
        man =  paginator.get_paginated_response(serializer.data)
        response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": man.data
            }
        return Response(response, status=status.HTTP_200_OK)

    
    if request.method == 'POST':
        serializer = taskserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": serializer.data
            }
        return Response(response, status=status.HTTP_200_OK)
        

    
@api_view(['GET','PUT','DELETE'])

def task_detail(request,id):
    try:
        emp = task.objects.get(pk=id)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = taskserializer(emp)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        serializer = taskserializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
##################################################################################################################

@api_view(['POST'])
def task_filter(request):
    try:
        if request.method == 'POST':
            serializer = task_filterserializer(data=request.data)
            if serializer.is_valid():
                project = serializer.validated_data.get('project')
                solution = serializer.validated_data.get('solution')
                feature = serializer.validated_data.get('feature')
                statuss = serializer.validated_data.get('statuss')
                stage = serializer.validated_data.get('stage')
                role = serializer.validated_data.get('role')
                dept = serializer.validated_data.get('dept')
                user = serializer.validated_data.get('user')
                
                taskf = task.objects.all()
                if project:
                    taskf = taskf.filter(project = project)
                
                if solution:
                    taskf = taskf.filter(solution = solution)
                
                if feature:
                    taskf = taskf.filter(feature = feature)

                if statuss:
                    taskf = taskf.filter(statuss = statuss)

                if stage:
                    taskf = taskf.filter(stage = stage)

                if role:
                    taskf = taskf.filter(role=role)
                
                if dept:
                    taskf = taskf.filter(dept=dept)

                if user:
                    taskf = taskf.filter(user = user)
                
                #task_data = taskserializer(tasf, many=True).data
                paginator = PageNumberPagination()
                paginator.page_size = 5
                result_page = paginator.paginate_queryset(taskf, request)
                task_data = taskserializer(result_page, many=True).data
                response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": task_data
                }
                
                #serializer = taskserializer(result_page, many = True)
                return paginator.get_paginated_response(response)

                #return Response(response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    