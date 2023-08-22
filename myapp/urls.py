from django.urls import path
from . import views

urlpatterns = [
    path('table/', views.table, name="table"),

    # category
    path('simple_page/category/', views.category, name="category"),
    path('category/change/<str:pk>/', views.category_change, name="category_change"),
    # posts
    path('', views.photo, name="photo"),
    path('photo/photo_create', views.photo_create, name="photo_create"),
    path('photo/photo_change/<str:pk>/', views.photo_change, name="photo_change"),

    
 
    

    
    ## nation
    path('nation/create', views.nation_create, name="nation"),
    path('natin/edit/<str:pk>/', views.nation_change, name="edit_nation"),
    path('natin/delete/<str:pk>/', views.remove_nation, name="remove_nation"),

    # current departments
    path('department/create', views.department_create, name="department"),
    path('department/change/<str:pk>/', views.department_change, name="department_edit"),
    path('department/delete/<str:pk>/', views.department_remove, name="department_remove"),

    # religion
    path('religion/create', views.create_religion, name="religionpage"),
    path('religion/edit/<str:pk>/', views.religion_change, name="religion_change"),
    path('religion/delete/<str:pk>/', views.remove_religion, name="remove_religion"),

    # training ground
    path('training_ground/create', views.create_training, name="training_ground"),
    path('train_ground/edit/<str:pk>/', views.change_training, name="training_ground_edit"),
    path('training/delete/<str:pk>/', views.remove_training, name="remove_training"),

    # training type
    path('training_type/create', views.create_type, name="training_type"),
    path('training_type/edit/<str:pk>/', views.change_type, name="change_type"),
    path('training_type/delete/<str:pk>/', views.remove_type, name="remove_type"),

    # serviced places
    path('rank/create', views.create_rank, name="rank"),
    path('rank/edit/<str:pk>/', views.change_rank, name="rank_change"),
    path('rank/delete/<str:pk>/', views.remove_rank, name="rank_delete"),


    # apppointment
    path('appointment/create', views.create_appointment, name="appointment"),
    path('appointment/edit/<str:pk>/', views.change_appointment, name="appointment_edit"),
    path('appointment/delete/<str:pk>/', views.remove_appointment, name="appointment_delete"),



    # blood
    path('blood/create', views.blood_create, name="blood"),
    path('blood/edit/<str:pk>/', views.change_blood, name="blood_change"),
    path('blood/delete/<str:pk>/', views.remove_blood, name="blood_delete"),


    # personal
    path('personal/', views.personal, name='personal_page'),
    path('personal/create', views.personal_create, name="personal_create"),
    path('personal/change/<str:pk>/', views.personal_change, name="personal_change"),
    path('personal/detail/<str:pk>/', views.personal_detail, name="personal_detail"),


    # crime add
    path('crime/<str:pk>/', views.crime, name="personal_crime_create"),
    path('crime/edit/<str:pk>/', views.crime_change, name="crime_edit"),



    # serviced
    path('serviced/<str:pk>/', views.serviced, name="personal_serviced_create"),
    path('serviced/edit/<str:pk>/', views.serviced_change, name="personal_serviced_edit"),


    # gender
    path('gender/create', views.gender_create, name='gender_page'),
    path('gender/edit/<str:pk>/', views.change_gender, name="gender_change"),
    path('gender/delete/<str:pk>/', views.remove_gender, name="remove_gender"),

    # married
    path('married/create', views.married_create, name='married_page'),
    path('married/edit/<str:pk>/', views.change_married, name="married_change"),
    path('married/delete/<str:pk>/', views.remove_married, name="remove_married"),









]
