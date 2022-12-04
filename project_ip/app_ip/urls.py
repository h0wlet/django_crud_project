from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('universities/', views.university_list),
    path('students/', views.student_list),

    path('universities/create/', views.create_university),
    path('universities/update/<int:univer_id>/', views.update_university),
    path('universities/delete/<int:univer_id>/', views.delete_university),

    path('students/create/', views.create_student),
    path('students/update/<int:stud_id>/', views.update_student),
    path('students/delete/<int:stud_id>/', views.delete_student),

]

