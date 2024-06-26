from rest_framework import serializers
from .models import role
from .models import dept
from .models import user

class roleserializer(serializers.ModelSerializer):
    class Meta:
        model = role
        fields = ['id','name']

class deptserializer(serializers.ModelSerializer):
    class Meta:
        model = dept
        fields = ['id','name']

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id','name']