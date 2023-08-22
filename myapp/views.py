from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

# Create your views here.

# category
def category(request):
    page = 'category_create'
    categories = Category.objects.all()
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('category')

    context = {
        'page':page,
        'categories':categories,
        'form':form

    }
    return render(request, 'simplepage/category.html', context)

def category_change(request, pk):
    page = 'category_change'
    categories = Category.objects.all()
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return redirect('category')

    context = {
        'page':page,
        'category':category,
        'form':form,
        'categories':categories

    }
    return render(request, 'simplepage/category.html', context)





def photo(request):
    photos = Photo.objects.all()
    
    context = {
        'photos':photos,
       
    }
    return render(request, 'simplepage/photo_index.html', context)

def photo_create(request):
    page = 'photo_create'
    photos = Photo.objects.all()
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('photo')

    context = {
        'page':page,
        'photos':photos,
        'form':form

    }
    return render(request, 'simplepage/photo.html', context)

def photo_change(request, pk):
    page = 'photo_change'
    photo = Photo.objects.get(id=pk)
    form = PhotoForm(instance=photo)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
        return redirect('photo')

    context = {
        'page':page,
        'photo':photo,
        'form':form

    }
    return render(request, 'simplepage/photo.html', context)

def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('photo')
    return render(request, 'auth/login_page.html', {'page':page})
 
def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(
                request, username=user.username, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return redirect('photo')

    context = {
        'form':form,
        'page':page
    }
    return render(request, 'auth/login_page.html', context)


def table(request):
    dashboard = Dashboard.objects.all()
    departments = Department.objects.all()
    bloods = Blood.objects.all()
    nations = Nation.objects.all()
    religions = Religion.objects.all()
    t_grounds = TrainingGround.objects.all()
    types = TrainingType.objects.all()
    ranks = Rank.objects.all()
    appointments = Appointment.objects.all()
    bloods = Blood.objects.all()
    crimes = Crime.objects.all()
    personals = Personal.objects.all()
    context = {
        'dashboard':dashboard,
        'nations':nations,
        'departments':departments,
        'bloods':bloods,
        'religions':religions,
        't_grounds':t_grounds,
        'types':types,
        'ranks':ranks,
        'appointments':appointments,
        'crimes':crimes,
        'personals':personals
    }
    return render(request, 'layout/table.html', context)


    



# start nation
# nation create

def nation_create(request):
    add = "add_nation"
    nations = Nation.objects.all()
    form = NationForm()
    if request.method == 'POST':
        form = NationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nation')
    context = {
        'nations':nations,
        'form':form,
        'add':add
    }
    return render(request, 'category/nation.html', context)

# edit nation
def nation_change(request, pk):
    change = "change_nation"
    nations = Nation.objects.all()
    nation = Nation.objects.get(id=pk)
    form = NationForm(instance=nation)
    if request.method == 'POST':
        form = NationForm(request.POST, instance=nation)
        if form.is_valid():
            form.save()
            return redirect('nation')

    context = {
            'change':change,
            'nations':nations,
            'nation':nation,
            'form':form
        }

    return render(request, 'category/nation.html', context)

# delete nation
def remove_nation(request, pk):
    nation = Nation.objects.get(id=pk)
    nation.delete()
    return redirect('nation')
    
# end nation



# current departments

def department_create(request):
    page = "add_depart"
    departments = Department.objects.all()
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department')
    context = {
        'page':page,
        'form':form,
        'departments':departments
    }
    return render(request, 'category/department.html', context)

# change departmets
def department_change(request, pk):
    change = "change_department"
    departments = Department.objects.all()
    department = Department.objects.get(id=pk)
    form = DepartmentForm(instance=department)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department')

    context = {
            'change':change,
            'departments':departments,
            'department':department,
            'form':form,
        }
    return render(request, 'category/department.html', context)

# delete departent
def department_remove(request, pk):
    department = Department.objects.get(id=pk)
    department.delete()
    return redirect('department')
# end department

# start religion
# create religion
def create_religion(request):
    add = 'add_religion'
    form = ReligionForm()
    religions = Religion.objects.all()
    if request.method == 'POST':
        form = ReligionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('religionpage')
    context = {
        'add':add,
        'form':form,
        'religions':religions
    }

    return render(request, 'category/religion.html', context)

# change religion
def religion_change(request, pk):
    change = "change_religion"
    religions = Religion.objects.all()
    religion = Religion.objects.get(id=pk)
    form = ReligionForm(instance=religion)
    if request.method == 'POST':
        form = ReligionForm(request.POST, instance=religion)
        if form.is_valid():
            form.save()
            return redirect('religionpage')

    context = {
            'change':change,
            'religions':religions,
            'religion':religion,
            'form':form,
        }
    return render(request, 'category/religion.html', context)

# delete
def remove_religion(request, pk):
    religion = Religion.objects.get(id=pk)
    religion.delete()
    return redirect('religionpage')
# end religion


# trainging ground
# create training

def create_training(request):
    add = "add_training"
    form = TrainingGroundForm()
    t_grounds = TrainingGround.objects.all()
    if request.method == 'POST':
        form = TrainingGroundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_ground')
    context = {
        'add':add,
        'form':form,
        't_grounds':t_grounds
    }
    return render(request, 'category/train_ground.html', context)

# change training
def change_training(request, pk):
    change = "change_training"
    t_grounds= TrainingGround.objects.all()
    t_ground = TrainingGround.objects.get(id=pk)
    form = TrainingGroundForm(instance=t_ground)
    if request.method == 'POST':
        form = TrainingGroundForm(request.POST, instance=t_ground)
        if form.is_valid():
            form.save()
            return redirect('training_ground')

    context = {
            'change':change,
            't_grounds':t_grounds,
            't_ground':t_ground,
            'form':form,
        }
    return render(request, 'category/train_ground.html', context)

# delete training
def remove_training(request, pk):
    t_ground = TrainingGround.objects.get(id=pk)
    t_ground.delete()
    return redirect('training_ground')


# training type
# create

def create_type(request):
    add = 'add_type'
    form = TrainingTypeForm()
    types = TrainingType.objects.all()
    if request.method == 'POST':
        form = TrainingTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_type')
    context = {
        'add':add,
        'form':form,
        'types':types
    }
    return render(request, 'category/train_type.html', context)

# edit
def change_type(request, pk):
    change = "change_type"
    types= TrainingType.objects.all()
    type = TrainingType.objects.get(id=pk)
    form = TrainingTypeForm(instance=type)
    if request.method == 'POST':
        form = TrainingTypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
            return redirect('training_type')

    context = {
            'change':change,
            'type':type,
            'types':types,
            'form':form,
        }
    return render(request, 'category/train_type.html', context)

# delete 
def remove_type(request, pk):
    type = TrainingType.objects.get(id=pk)
    type.delete()
    return redirect('training_type')

# rank
# create

def create_rank(request):
    add = 'add_rank'
    form = RankForm()
    ranks = Rank.objects.all() 
    if request.method == 'POST':
        form = RankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rank')
    context = {
        'add':add,
        'form':form,
        'ranks':ranks
    }
    return render(request, 'category/rank.html', context)

# edit
def change_rank(request, pk):
    change = "change_rank"
    ranks= Rank.objects.all()
    rank = Rank.objects.get(id=pk)
    form = RankForm(instance=rank)
    if request.method == 'POST':
        form = RankForm(request.POST, instance=rank)
        if form.is_valid():
            form.save()
            return redirect('rank')

    context = {
            'change':change,
            'rank':rank,
            'ranks':ranks,
            'form':form,
        }
    return render(request, 'category/rank.html', context)

# delete
def remove_rank(request, pk):
    
    rank = Rank.objects.get(id=pk)
    rank.delete()
    return redirect('rank')


# appointment
# create

def create_appointment(request):
    add = 'add_appointment'
    form = AppointmentForm()
    appointments = Appointment.objects.all()
    page = request.GET.get('page', 1)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment')
    # paginator code 
    paginator = Paginator(appointments, 2)
    try:
      appointments = paginator.page(page)
    except PageNotAnInteger:
      appointments = paginator.page(1)
    except EmptyPage:
      appointments=paginator.page(paginator.num_pages)
    context = {
        'add':add,
        'form':form,
        'appointments':appointments
    }
    return render(request, 'category/appointment.html', context)


# edit
def change_appointment(request, pk):
    change = "change_appointment"
    appointments= Appointment.objects.all()
    appointment = Appointment.objects.get(id=pk)
    form = AppointmentForm(instance=appointment)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment')

    context = {
            'change':change,
            'appointment':appointment,
            'appointments':appointments,
            'form':form,
        }
    return render(request, 'category/appointment.html', context)

# delete
def remove_appointment(request, pk):
    
    appointment = Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('appointment')
# end appointment






# blood
# create

def blood_create(request):
    add = 'add_blood'
    form = BloodForm()
    bloods = Blood.objects.all()
    if request.method == 'POST':
        form = BloodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blood')
    context = {
        'add':add,
        'form':form,
        'bloods':bloods
    }
    return render(request, 'category/blood.html', context)

def change_blood(request, pk):
    change = "change_blood"
    bloods= Blood.objects.all()
    blood = Blood.objects.get(id=pk)
    form = BloodForm(instance=blood)
    if request.method == 'POST':
        form = BloodForm(request.POST, instance=blood)
        if form.is_valid():
            form.save()
            return redirect('blood')

    context = {
            'change':change,
            'bloods':bloods,
            'blood':blood,
            'form':form,
        }
    return render(request, 'category/blood.html', context)

# delete
def remove_blood(request, pk):
    
    blood = Blood.objects.get(id=pk)
    blood.delete()
    return redirect('blood')
# end appointment


# personal 


# gender

def gender_create(request):
    add = 'add_gender'
    form = GenderForm()
    genders = Gender.objects.all()
    if request.method == 'POST':
        form = GenderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gender_page')
    context = {
        'add':add,
        'form':form,
        'genders':genders
    }
    return render(request, 'category/gender.html', context)
# change
def change_gender(request, pk):
    change = "change_gender"
    genders= Gender.objects.all()
    gender = Gender.objects.get(id=pk)
    form = GenderForm(instance=gender)
    if request.method == 'POST':
        form = GenderForm(request.POST, instance=gender)
        if form.is_valid():
            form.save()
            return redirect('gender_page')

    context = {
            'change':change,
            'genders':genders,
            'gender':gender,
            'form':form,
        }
    return render(request, 'category/gender.html', context)

# delete gender
def remove_gender(request, pk):
    
    gender = Gender.objects.get(id=pk)
    gender.delete()
    return redirect('gender_page')


# married

def married_create(request):
    add = 'add_married'
    form = MarriedForm()
    marrieds = Married.objects.all()
    if request.method == 'POST':
        form = MarriedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('married_page')
    context = {
        'add':add,
        'form':form,
        'marrieds':marrieds
    }
    return render(request, 'category/married.html', context)
# change
def change_married(request, pk):
    change = "change_married"
    marrieds= Married.objects.all()
    married = Married.objects.get(id=pk)
    form = MarriedForm(instance=married)
    if request.method == 'POST':
        form = MarriedForm(request.POST, instance=married)
        if form.is_valid():
            form.save()
            return redirect('married_page')

    context = {
            'change':change,
            'marrieds':marrieds,
            'married':married,
            'form':form,
        }
    return render(request, 'category/married.html', context)

# delete gender
def remove_married(request, pk):
    
    married = Gender.objects.get(id=pk)
    married.delete()
    return redirect('married_page')


def personal(request):
    personals = Personal.objects.all()
    new_search = request.GET.get('search') if request.GET.get('search') != None else''
    personal_search = Personal.objects.filter(
        Q(name__contains = new_search)|
        Q(department__name__contains = new_search)|
        Q(batch_no__contains = new_search)|
        Q(blood__name__contains = new_search)|
        Q(religion__name__contains = new_search)|
        Q(blood__name__contains = new_search)|
        Q(gender__name__contains = new_search)|
        Q(married__name__contains = new_search)|
        Q(nation__name__contains = new_search)
      
        

    )
    # paginator code 
    page = request.GET.get('page', 1)
    paginator = Paginator(personals, 1)
    try:
      personals = paginator.page(page)
    except PageNotAnInteger:
      personals = paginator.page(1)
    except EmptyPage:
      personals=paginator.page(paginator.num_pages)
    form =PersonalForm()
    context = {
        'new_search':new_search,
        'personals':personals,
        'personal_search':personal_search,
        'form':form, 
       
        
    }
    return render(request, 'personal/index.html', context)

    
# create

def personal_create(request):
    add = "personal_add"
    personals = Personal.objects.all()
    form = PersonalForm()
    if request.method == 'POST':
        form = PersonalForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('personal_page')
    context = {
        'add':add,
        'form':form,
        'personals':personals
    }
    return render(request, 'personal/personal_create.html', context)

def personal_change(request, pk):
    personal = Personal.objects.get(id=pk)
    personals = Personal.objects.all()
    form = PersonalForm(instance=personal)
    if request.method == 'POST':
        form = PersonalForm(request.POST,request.FILES, instance=personal)
        if form.is_valid():
            form.save()
        return redirect('personal_page')
    context = {
        'personal':personal,
        'form':form,
        'personals':personals
    }
    return render(request, 'personal/personal_change.html', context)

def personal_detail(request, pk):
    personal = Personal.objects.get(id=pk)
    personals = Personal.objects.all()
    crime = Crime.objects.filter(name_id=pk)
    serviced = ServicedPlace.objects.filter(name_id=pk)
    form = PersonalForm(instance=personal)
    
    context = {
        'personal':personal,
        'form':form,
        'personals':personals,
        'crime':crime,
        'serviced':serviced,
        
    }
    return render(request, 'personal/personal_detail.html', context)

# create -crime

def crime(request, pk):
    crime = Crime.objects.all()
    form = CrimeForm()
    personal = Personal.objects.get(id=pk)
    if request.method == 'POST':
        form = CrimeForm(request.POST)
        if form.is_valid():
            form.instance.personal_id =pk
            form.save()
            return redirect('personal_page')
    context = {
        'form':form,
        'crime':crime,
        'personal':personal
    }
    return render(request, 'personal/crime/crime_create.html', context)

# edit -crime
def crime_change(request, pk):
    crimes = Crime.objects.all()
    crime = Crime.objects.get(id=pk)
    form = CrimeForm(instance=crime)
    if request.method == 'POST':
        form = CrimeForm(request.POST, instance=crime)
        if form.is_valid():
            form.instance.personal_id =pk
            form.save()
            return redirect('personal_page')
    context = {
        'form':form,
        'crimes':crimes,
        'crime':crime,
        'personal':personal
    }
    return render(request, 'personal/crime/crime_edit.html', context)


# create -serviced
def serviced(request, pk):
    serviced= ServicedPlace.objects.all()
    form = Serviced_Form()
    personal = Personal.objects.get(id=pk)
    if request.method == 'POST':
        form = Serviced_Form(request.POST)
        if form.is_valid():
            form.instance.personal_id =pk
            form.save()
            return redirect('personal_page')
    context = {
        'form':form,
        'serviced':serviced,
        'personal':personal
    }
    return render(request, 'personal/serviced/serviced_create.html', context)

def serviced_change(request, pk):
    serviceds = ServicedPlace.objects.all()
    serviced = ServicedPlace.objects.get(id=pk)
   
    form = Serviced_Form(instance=serviced)
    if request.method == 'POST':
        form = Serviced_Form(request.POST, instance=serviced)
        if form.is_valid():
            form.instance.personal_id =pk
            form.save()
            return redirect('personal_page')
    context = {
        'form':form,
        'serviced':serviced,
        'serviceds':serviceds,
        
       
    }
    return render(request, 'personal/serviced/serviced_change.html', context)

