from django.contrib import admin
from . models import *

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name', 'age', 'address', 'contact', 'current_class', 'major', 'image']



admin.site.register(Student, StudentAdmin)
