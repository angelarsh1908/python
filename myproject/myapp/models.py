# from curses import ACS_GEQUAL
# from curses import *
# import email
# from statistics import mode
from tkinter import CASCADE
from turtle import mode
from xml.parsers.expat import model
from django.db import models
from .models import models

class user(models.Model):
    email=models.EmailField(unique=True,max_length=40)
    password=models.CharField(max_length=30)
    role=models.CharField(max_length=30)
    otp=models.IntegerField(default=456)
    is_verify=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True,null=True )

    def __str__(self) -> str:
        return self.email

class Doctor(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    qualification=models.CharField(max_length=50,blank=True,null=True)
    specification=models.CharField(max_length=50,blank=True,null=True)
    available_time=models.CharField(max_length=50,blank=True,null=True)
    experience=models.CharField(max_length=50,blank=True,null=True)
    clinic_name=models.CharField(max_length=50,blank=True,null=True)
    clinic_city=models.CharField(max_length=50,blank=True,null=True)
    clinic_address=models.TextField(blank=True,null=True)
    mobile=models.CharField(max_length=20,blank=True,null=True)
    # pic=models.FileField(upload_to="media/images",default="media/difault_pic.png")
    pic=models.FileField(upload_to="media/images",default="media/ddd.png")

    def __str__(self) -> str:
        return self.firstname
    
# class patient(models.Model):
#     user_id=models.ForeignKey(user,on_delete=models.CASCADE)
#     firstname=models.CharField(max_length=30)
#     lastname=models.CharField(max_length=30)
#     age=models.CharField(max_length=50,blank=True,null=True)
#     gender=models.CharField(max_length=50,blank=True,null=True)
#     birthdate=models.DateField(auto_created=True,null=True)
#     bloodgroup=models.CharField(max_length=50,blank=True,null=True)
#     height=models.CharField(max_length=20,blank=True,null=True)
#     weight=models.CharField(max_length=20,blank=True,null=True)
#     mobile=models.CharField(max_length=20,blank=True,null=True)
#     address=models.TextField(blank=True,null=True)
#     pic=models.TextField(blank=True,null=True)

class Patient(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    age=models.CharField(max_length=50,blank=True,null=True)
    gender=models.CharField(max_length=50,blank=True,null=True)
    birthdate=models.DateField(auto_created=True,null=True)
    bloodgroup=models.CharField(max_length=50,blank=True,null=True)
    height=models.CharField(max_length=20,blank=True,null=True)
    weight=models.CharField(max_length=20,blank=True,null=True)
    mobile=models.CharField(max_length=20,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    pic = models.FileField(upload_to="media/images", default="media/ddd.png")

    def __str__(self) -> str:
        return self.firstname

class Appointment(models.Model):
    patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    a_date=models.DateField(max_length=20)
    a_time=models.CharField(max_length=30)
    reason=models.TextField()
    status=models.CharField(max_length=30,default="PENDING") 
    doc_note=models.TextField(blank=True)
    case_status=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.patient_id.firstname + "" + self.patient_id.lastname