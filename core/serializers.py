from rest_framework import serializers 
from .models import project
from .models import solution
from .models import feature
from .models import task


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