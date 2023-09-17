from .views import listAll2,IdList2
from django.urls import path

urlpatterns = [
    path("all2/",listAll2.as_view()),
    path("Id2/",IdList2.as_view())
]