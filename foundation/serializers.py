from rest_framework import serializers 
from .models import statuss
from .models import stage


class statussserializer(serializers.ModelSerializer):
    class Meta:
        model = statuss
        fields = ['id','name']

class stageserializer(serializers.ModelSerializer):
    class Meta:
        model = stage
        fields = ['id','name']
