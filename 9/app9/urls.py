from django.urls import path 
from .views import AllList9,Idlist9

urlpatterns = [
    path("app9/",AllList9.as_view()),
    path("app9",Idlist9.as_view())

]