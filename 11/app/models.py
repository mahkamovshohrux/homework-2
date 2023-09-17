from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Models11(models.Model):
    name11 = models.CharField(max_length=30,)
    lastname11 = models.CharField(max_length=30,)
    deta11 = models.DateField(default=datetime.now)
    user11 = models.ForeignKey(User,on_delete=models.CASCADE,default="")
    def __str__(self) -> str:
        return self.name11

