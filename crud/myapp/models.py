from django.db import models
from django.db import models
from .models import models

# Create your models here.
class log(models.Model):
    email=models.EmailField(unique=True,max_length=40)
    password=models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.email

class Register(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    gender=models.CharField(max_length=50,blank=True,null=True)
    language=lastname=models.CharField(max_length=30)
    city=models.TextField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    def __str__(self) -> str:
       return self.firstname
