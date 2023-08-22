from django.db import models
from datetime import datetime
# from django.contrib.auth.models import User
from accounts.models import *


 
# Create your models here.

# category
class Category(models.Model):
   user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
   name = models.CharField(max_length=100, null=True, blank=True)

   def __str__(self):
      return self.name

class Photo(models.Model):
   category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
   country = models.CharField(max_length=50, null=True, blank=True)
   image = models.ImageField(upload_to='category-photo',null=True, blank=True)
   title = models.CharField(max_length=50,null=True, blank=True)

   def __str__(self):
      return self.description
# finished
class Nation(models.Model):  
   name = models.CharField(max_length=200)

   def __str__(self):
      return self.name

# finished
class Department(models.Model):
   name = models.CharField(max_length=200)

   def __str__(self):
      return self.name
   
# finished
class TrainingGround(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name
   
# finished
class TrainingType(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name

# finished
class Rank(models.Model):
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name
   
# finished
class Religion(models.Model):
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name

# finished
class Appointment(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name

   
class Blood(models.Model):
   name = models.CharField(max_length=10)

   def __str__(self):
      return self.name

class Dashboard(models.Model):
   name = models.CharField(max_length=20)

   def __str__(self):
      return self.name
   
class Town(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name

class Married(models.Model):
   name = models.CharField(max_length=25)

   def __str__(self):
      return self.name
   
class Gender(models.Model):
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name
   
class Personal(models.Model):
   name = models.CharField(max_length=50)
   rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
   appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True)
   ser_number = models.CharField(max_length=50)
   image = models.ImageField(upload_to='personal-image', null=True, blank=True)
   department = models.ForeignKey(Department, on_delete=models.CASCADE)
   gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
   birthday = models.DateField(null=True, blank=True)
   religion = models.ForeignKey(Religion, on_delete=models.CASCADE, null=True, blank=True)
   nation = models.ForeignKey(Nation,on_delete=models.CASCADE)
   address = models.CharField(max_length=100)
   father = models.CharField(max_length=100)
   mother = models.CharField(max_length=100)
   married = models.ForeignKey(Married, on_delete=models.CASCADE)
   blood = models.ForeignKey(Blood, on_delete=models.CASCADE)
   health = models.CharField(max_length=50)
   height = models.CharField(max_length=50)
   education = models.CharField(max_length=100)
   join_date = models.DateField(null=True, blank=True)
   batch_no = models.CharField(max_length=50)
   trained_place = models.ForeignKey(TrainingGround, on_delete=models.CASCADE)
   trained_type = models.ManyToManyField(TrainingType)
   long_time = models.CharField(max_length=20, null=True, blank=True)
   

   def __str__(self):
      return self.name
   
 
   @property
   def birthdayCount (self):
        return int((datetime.now().date()-self.birthday).days/365.25)
   
   @property
   def join_dateCount(self):
      return int((datetime.now().date()-self.join_date).days/365.25)
   
class Crime(models.Model):
   name = models.ForeignKey(Personal, on_delete=models.CASCADE)
   crime_type = models.CharField(max_length=255, null=True, blank=True)
   punished = models.CharField(max_length=255, blank=True, null=True)
   start = models.DateField(null=True, blank=True)
   end = models.DateField(null=True, blank=True)
   commander = models.CharField(max_length=200, null=True, blank=True)

   def __str__(self):
      return self.crime_type

   @property
   def startCount (self):
        return int((datetime.now().date()-self.start).days/365.25)
        
   @property
   def endCount (self):
        return int((datetime.now().date()-self.end).days/365.25)


class ServicedPlace(models.Model):
   name = models.ForeignKey(Personal, on_delete=models.CASCADE)
   serviced = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
   start_date = models.DateField(null=True, blank=True)
   end_date = models.DateField(null=True, blank=True)
   long_time = models.CharField(max_length=255, null=True, blank=True)

   def __str__(self):
      return self.serviced

   @property
   def start_dateCount (self):
        return int((datetime.now().date()-self.start_date).days/365.25)
        
   @property
   def end_dateCount (self):
        return int((datetime.now().date()-self.end_date).days/365.25)