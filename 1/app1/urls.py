from django.urls import path
from .views import ListAll,IdList

urlpatterns =[
    path("all/", ListAll.as_view()),
    path("id/",IdList.as_view())
]