from django.shortcuts import render
from rest_framework import generics
from .models import Models8
from .serialisers import Serializers8
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class AllList8(generics.ListAPIView):
    queryset = Models8.objects.all()
    serializer_class = Serializers8
    permission_classes = (IsAuthenticated,)
class Idlist8(generics.CreateAPIView):
    queryset = Models8.objects.all()
    serializer_class = Serializers8
