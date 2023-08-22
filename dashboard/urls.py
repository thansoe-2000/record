from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    
    # student urls
    path('create_student/', views.student_create, name="create_student"),
    path('detail_student/<str:pk>/', views.student_detail, name="detail_student"),
    path('change_student/<str:pk>/', views.student_change, name="student_change"),

    # father urls
    path('father_create/', views.father_create, name="father_create"),
    



]
