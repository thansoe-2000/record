from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import *

# Register your models here.
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email','username','profile','is_staff',]
admin.site.register(CustomUser,CustomUserAdmin)