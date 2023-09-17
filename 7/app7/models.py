from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Models7(models.Model):
    name7 = models.CharField(max_length=40)
    lastname7 = models.CharField(max_length=20)
    data7 = models.DateField()
    user7 = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    def __str__(self) -> str:
        return self.name7
