from django.urls import path
from . import views

urlpatterns = [
    path('many_form/', views.many_form, name="many_form"),
   
]
