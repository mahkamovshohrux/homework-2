from django.shortcuts import render 
from rest_framework import generics
from .models import Models1
from .serializers import Serializers1
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ListAll(generics.ListAPIView):
    queryset = Models1.objects.all()
    serializer_class = Serializers1
    permission_classes = (IsAuthenticated,)

class IdList(generics.CreateAPIView):
    queryset = Models1.objects.all()
    serializer_class = Serializers1
