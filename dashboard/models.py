from django.db import models
from datetime import datetime
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    current_class = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    image = models.ImageField(upload_to='student-image', null=True, blank=True)

    # father
    f_name = models.CharField(max_length=100, null=True, blank=True)
    f_age = models.DateField(null=True, blank=True)
    f_careers = models.CharField(max_length=100, null=True, blank=True)
    f_address = models.CharField(max_length=200, null=True, blank=True)
    f_contact = models.CharField(max_length=100, null=True, blank=True)
    f_image = models.ImageField(upload_to='father-image', null=True, blank=True)

    # mother
    m_name = models.CharField(max_length=100, null=True, blank=True)
    m_age = models.DateField(null=True, blank=True)
    m_careers = models.CharField(max_length=100, null=True, blank=True)
    m_address = models.CharField(max_length=100, null=True, blank=True)
    m_contact = models.CharField(max_length=100, null=True, blank=True)
    m_image = models.ImageField(upload_to='mother-image', null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def ageCount (self):
        return int((datetime.now().date()-self.age).days/365.25)

    @property
    def f_ageCount (self):
        return int((datetime.now().date()-self.f_age).days/365.25)
    @property
    def m_ageCount (self):
        return int((datetime.now().date()-self.m_age).days/365.25)