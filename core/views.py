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

                page_no = int(request['Page_No'])
                no_of_data = int(request['No_Of_Data'])
                #task_data = taskserializer(tasf, many=True).data
                paginator = PageNumberPagination()
                paginator.page_size = 5
                result_page = paginator.paginate_queryset(taskf, request)
                task_data = taskserializer(result_page, many=True).data
                #paginated_data = paginator.get_paginated_response(task_data)
                #print(paginated_data)
                data = Paginator(data,no_of_data).page(page_no)

                response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": data
                }
                
                #serializer = taskserializer(result_page, many = True)
                return paginator.get_paginated_response(response)

                #return Response(response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    
    
'''
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
'''


error_message = 'Something went wrong. Please try again later.'
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer

class BookListCreate(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###################################################################################################################
from .models import Client
from .serializers import ClientSerializer

class ClientListCreate(APIView):
    def get(self, request):
        enter = Client.objects.all()
        serializer = ClientSerializer(enter, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": "Client provided successfully",
                "data": serializer.data
        }
        return Response(response)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": "Client added successfully",
                "data": serializer.data
            }
            return Response(response)
        error = {
                "status": False,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "status_message": error_message,
                "error": serializer.errors
            }
        return Response(error)
    
class ClientDetail(APIView):
    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        enter = self.get_object(pk)
        serializer = ClientSerializer(enter)
        return Response(serializer.data)

    def put(self, request, pk):
        enter = self.get_object(pk)
        serializer = ClientSerializer(enter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        enter = self.get_object(pk)
        enter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
################################################################################################################
from .models import Department
from .serializers import DepartmentSerializer
class DepartmentListCreate(APIView):
    def get(self, request):
        enter = Department.objects.all()
        serializer = DepartmentSerializer(enter, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": "Department provided successfully",
                "data": serializer.data
        }
        return Response(response)
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": "Department added successfully",
                "data": serializer.data
            }
            return Response(response)
        error = {
                "status": False,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "status_message": error_message,
                "error": serializer.errors
            }
        return Response(error)
    
class DepartmentDetail(APIView):
    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        enter = self.get_object(pk)
        serializer = DepartmentSerializer(enter)
        return Response(serializer.data)

    def put(self, request, pk):
        enter = self.get_object(pk)
        serializer = DepartmentSerializer(enter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        enter = self.get_object(pk)
        enter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
################################################################################################################
from .models import Designation
from .serializers import DesignationSerializer
class DesignationListCreate(APIView):
    def get(self, request):
        enter = Designation.objects.all()
        serializer = DesignationSerializer(enter, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DesignationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DesignationDetail(APIView):
    def get_object(self, pk):
        try:
            return Designation.objects.get(pk=pk)
        except Designation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        enter = self.get_object(pk)
        serializer = DesignationSerializer(enter)
        return Response(serializer.data)

    def put(self, request, pk):
        enter = self.get_object(pk)
        serializer = DesignationSerializer(enter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        enter = self.get_object(pk)
        enter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
################################################################################################################
#####################################################################################################################

from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
class UserListCreate(APIView):
    def get(self, request):
        enter = User.objects.all()
        serializer = UserSerializer(enter, many=True)
        response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": "User provided successfully",
                "data": serializer.data
        }
        return Response(response)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": True,
                "status_code": status.HTTP_200_OK,
                "status_message": "User added successfully",
                "data": serializer.data
            }
            return Response(response)
        error = {
                "status": False,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "status_message": error_message,
                "error": serializer.errors
            }
        return Response(error)
    
class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        enter = self.get_object(pk)
        serializer = UserSerializer(enter)
        return Response(serializer.data)

    def put(self, request, pk):
        enter = self.get_object(pk)
        serializer = UserSerializer(enter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        enter = self.get_object(pk)
        enter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
################################################################################################################


