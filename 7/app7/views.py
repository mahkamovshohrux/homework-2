from django.shortcuts import render
from rest_framework import generics
from .models import Models7
from .serializers import Serializers7
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class AllList7(generics.ListAPIView):
    queryset = Models7.objects.all()
    serializer_class = Serializers7
    permission_classes = (IsAuthenticated,)
class Idlist7(generics.CreateAPIView):
    queryset = Models7.objects.all()
    serializer_class = Serializers7
