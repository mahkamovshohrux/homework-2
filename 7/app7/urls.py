from django.urls import path 
from .views import AllList7,Idlist7

urlpatterns = [
    path("app7/",AllList7.as_view()),
    path("app7",Idlist7.as_view())

]