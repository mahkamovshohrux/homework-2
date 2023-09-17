from .models import Models1
from rest_framework import serializers 
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class Serializers1(serializers.ModelSerializer):
    class Meta:
        model = Models1
        fields = ('name','lastname','deta','user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User,username=self.context['request'].user)
        return super(Serializers1,self).create(validated_data)