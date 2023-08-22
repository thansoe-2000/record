from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
     profile = models.ImageField(upload_to = "profiles/", blank=True,null=True,default="static/assets/images/dashboard/img_3.jpg")

     @property
     def userimageURL(self):
          try:
               url = self.profile.url
          except:
               url = ''

          return url