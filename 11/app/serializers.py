from .models import Models11
from rest_framework import serializers 
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class Serializers11(serializers.ModelSerializer):
    class Meta:
        model = Models11
        fields = ('name11','lastname11','deta11','user11')

    def create(self, validated_data):
        validated_data['user11']=get_object_or_404(User,username=self.context['request'].user)
        return super(Serializers11,self).create(validated_data)