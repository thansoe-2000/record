from django.contrib import admin
from . models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
   list_display = ['id', 'name']

class PhotoAdmin(admin.ModelAdmin):
   list_display = ['id', 'category', 'title','country', 'image']

class NationAdmin(admin.ModelAdmin):
   list_display = ['id', 'name']


class Department_Admin(admin.ModelAdmin):
   list_display = ['id', 'name']


class TrainingGround_Admin(admin.ModelAdmin):
   list_display = ['id', 'name']


class TrainingType_Admin(admin.ModelAdmin):
   list_display = ['id', 'name']

class RankAdmin(admin.ModelAdmin):
   list_display = [ 'id', 'name']


class ReligionAdmin(admin.ModelAdmin):
   list_display = [ 'id', 'name']

class AppointmentAdmin(admin.ModelAdmin):
   list_display = [ 'id', 'name']

class CrimeAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'crime_type', 'punished', 'start', 'end', 'commander']

class BloodAdmin(admin.ModelAdmin):
   list_display = [ 'id', 'name']

class DashboardAdmin(admin.ModelAdmin):
   list_display = [ 'id', 'name']

class TownAdmin(admin.ModelAdmin):
   list_display = ['id', 'name'] 

class PersonalAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'image']

class MarriedAdmin(admin.ModelAdmin):
   list_display = [ 'id', 'name']

class GenderAdmin(admin.ModelAdmin):
   list_display = ['id', 'name']

class ServicedPlaceAdmin(admin.ModelAdmin):
   list_display = [ 'id', 'name']

admin.site.register(Nation, NationAdmin)
admin.site.register(Department, Department_Admin)
admin.site.register(TrainingGround, TrainingGround_Admin)
admin.site.register(TrainingType, TrainingType_Admin)
admin.site.register(Rank, RankAdmin)
admin.site.register(Religion, ReligionAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Crime, CrimeAdmin)
admin.site.register(Blood, BloodAdmin)
admin.site.register(Dashboard, DashboardAdmin)
admin.site.register(Town, TownAdmin)
admin.site.register(Personal)
admin.site.register(Married, MarriedAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(ServicedPlace, ServicedPlaceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)

