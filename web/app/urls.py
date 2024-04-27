from django.urls import path
from . import views

urlpatterns = [ 

    path('',views.main),
    path('LogIn/', views.LogIn, name='logIn'),
    path('Register/', views.Register, name='Register'),  
    path('Course/',views.Course, name='course'),
    path('Search/',views.Search , name='search'),
    path('Course_details/',views.Course_details, name='course_details'),
    path('main/',views.main , name='main'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
]
  




