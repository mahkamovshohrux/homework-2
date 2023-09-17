from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Models8(models.Model):
    name8 = models.CharField(max_length=40)
    lastname8 = models.CharField(max_length=20)
    data8 = models.DateField()
    user8 = models.ForeignKey(User,on_delete=models.CASCADE,default="")
    def __str__(self) -> str:
        return self.name8
