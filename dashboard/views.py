from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def dashboard(request):
    students = Student.objects.all()
    context = {
        'students':students
    }
    return render(request, 'dashboard/dashboard.html', context)
# student personal start
def student_create(request):
    add = "add_student"
    students = Student.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'add':add,
        'students':students,
        'form':form
    }
    return render(request, 'dashboard/action.html', context)

def student_change(request, pk):
    change = "student_change"
    student = Student.objects.get(id=pk)
    students = Student.objects.all()
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
        return redirect('dashboard')
    context = {
        'change':change,
        'student':student,
        'students':students,
        'form':form
    }
    return render(request, 'dashboard/action.html', context)

def student_detail(request, pk):
    detail = "student_detail"
    
    student = Student.objects.get(id=pk)
    
    students = Student.objects.all()
    
    form = StudentForm(instance=student)
    context = {
        'student':student,
        'students':students,
        'form':form,
        'detail':detail
        
    }
    return render(request, 'dashboard/action.html', context)

# end student personal

# start father personal

def father_create(request):
    create = "create_father"
    father = Student.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'create':create,
        'father':father,
        'form':form
    }
    return render(request, 'dashboard/father.html', context)
