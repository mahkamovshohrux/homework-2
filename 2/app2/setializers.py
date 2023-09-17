from .models import Models2
from rest_framework import serializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class Serializers2(serializers.ModelSerializer):
    class Meta:
        model = Models2
        fields = ('name2','lastname2','data2','user')
    
    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User,username=self.context['request'].user)
        return super(Serializers2,self).create(validated_data)