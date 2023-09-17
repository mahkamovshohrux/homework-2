from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Models2(models.Model):
    name2 = models.CharField(max_length=30,)
    lastname2 = models.CharField(max_length=30,)
    data2 = models.DateField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=3)
    def __str__(self) -> str:
        return self.name2
