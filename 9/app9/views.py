from django.shortcuts import render
from rest_framework import generics
from .models import Models9
from .serializers import Serializers9
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class AllList9(generics.ListAPIView):
    queryset = Models9.objects.all()
    serializer_class = Serializers9
    permission_classes = (IsAuthenticated,)
class Idlist9(generics.CreateAPIView):
    queryset = Models9.objects.all()
    serializer_class = Serializers9
