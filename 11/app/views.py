from django.shortcuts import render 
from rest_framework import generics
from .models import Models11
from .serializers import Serializers11
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ListAll11(generics.ListAPIView):
    queryset = Models11.objects.all()
    serializer_class = Serializers11
    permission_classes = (IsAuthenticated,)

class IdList11(generics.CreateAPIView):
    queryset = Models11.objects.all()
    serializer_class = Serializers11
