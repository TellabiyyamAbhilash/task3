from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)

class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key=True)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    profilepicture  = models.ImageField(upload_to='static/images',null=True,blank=True)
    Address_line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    last_login = models.CharField(max_length=100,default=True)
    def get_absolute_url(self):
        return reverse('docdetails',kwargs={'pk':self.pk})


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    profilepicture  = models.ImageField(upload_to='static/images',null=True,blank=True)
    Address_line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    last_login = models.CharField(max_length=100,default=True)
    def get_absolute_url(self):
        return reverse('patdetails',kwargs={'pk':self.pk})

class Category (models.Model):
    name=models.CharField(max_length=100)

class Blog(models.Model):
    title = models.CharField(max_length=100,null=False,blank=False)
    image = models.ImageField(upload_to='static/images',null=False,blank=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=True,null=False)
    summary = models.TextField(max_length=1000)
    content = models.CharField(max_length=250)
    def get_absolute_url(self):
        return reverse('blog',kwargs={'pk':self.pk})

class Appointment(models.Model):
    speciality = models.CharField(max_length=100,null=False,blank=False)
    date = models.DateField()
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,default=True,null=False)
    time = models.TimeField()

    def get_absolute_url(self):
        return reverse('appointment',kwargs={'pk':self.pk})
