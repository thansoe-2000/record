from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def many_form(request):
    return render(request, 'many_form/add_form.html') 

