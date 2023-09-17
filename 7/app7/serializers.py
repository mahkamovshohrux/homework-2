from rest_framework import serializers
from .models import Models7
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class Serializers7(serializers.ModelSerializer):
    class Meta:
        model = Models7
        fields = ('name7','lastname7','data7','user7')


    def create(self, validated_data):
        validated_data['user7'] = get_object_or_404(User,username=self.context['request'].user)
        return super(Serializers7,self).create(validated_data)