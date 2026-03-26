from django.urls import path  
from . import views  

urlpatterns = [  
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'),
    
    path('employees/', views.employee_list, name='employees'), 
    path('students/', views.student_list, name='students'),
    path('form/',views.form,name='form'),
    path('result/', views.result, name='result'),

    path('vistor/',views.vistor,name='vistor'),
    path('results/', views.results, name='results'),]
