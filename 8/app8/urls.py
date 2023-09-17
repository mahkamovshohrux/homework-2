from django.urls import path 
from .views import AllList8,Idlist8

urlpatterns = [
    path("app8/",AllList8.as_view()),
    path("app8",Idlist8.as_view())

]