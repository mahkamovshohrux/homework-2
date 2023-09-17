from rest_framework import serializers
from .models import Models9
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class Serializers9(serializers.ModelSerializer):
    class Meta:
        model = Models9
        fields = ('name9','lastname9','data9','user9')

    def create(self, validated_data):
        validated_data['user9']=get_object_or_404(User,username=self.context['request'].user)
        return super(Serializers9,self).create(validated_data)