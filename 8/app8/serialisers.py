from rest_framework import serializers
from .models import Models8
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class Serializers8(serializers.ModelSerializer):
    class Meta:
        model = Models8
        fields = ('name8','lastname8','data8','user8')

    def create(self, validated_data):
        validated_data['user8'] =get_object_or_404(User, username=self.context['request'].user)
        return super(Serializers8,self).create(validated_data)