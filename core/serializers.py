from rest_framework import serializers 
from .models import project
from .models import solution
from .models import feature
from .models import task
from .models import Book

class projectserializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ['id','name']

class solutionserializer(serializers.ModelSerializer):
    class Meta:
        model = solution
        fields = ['id','name','project']

class featureserializer(serializers.ModelSerializer):
    class Meta:
        model = feature
        fields = ['id','name','project','solution']

class taskserializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ['id','name','project','solution','feature','statuss','stage','role','dept','user']

class task_filterserializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ['project','solution','feature','statuss','stage','role','dept','user']



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
from .models import Department
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
from .models import Designation
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'