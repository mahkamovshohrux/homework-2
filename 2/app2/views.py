from django.shortcuts import render
from rest_framework import generics
from .setializers import Serializers2
from .models import Models2
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class listAll2(generics.ListAPIView):
    queryset = Models2.objects.all()
    serializer_class = Serializers2
    permission_classes = (IsAuthenticated,)

class IdList2(generics.CreateAPIView):
    queryset = Models2.objects.all()
    serializer_class = Serializers2
