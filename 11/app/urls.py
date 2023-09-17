from django.urls import path
from .views import ListAll11,IdList11

urlpatterns =[
    path("all/", ListAll11.as_view()),
    path("id/",IdList11.as_view())
]