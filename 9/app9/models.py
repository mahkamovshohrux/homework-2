from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Models9(models.Model):
    name9 = models.CharField(max_length=40)
    lastname9 = models.CharField(max_length=20)
    data9 = models.DateField()
    user9 = models.ForeignKey(User,on_delete=models.CASCADE,default="")
    def __str__(self) -> str:
        return self.name9
