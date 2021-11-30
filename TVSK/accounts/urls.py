from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/', views.home, name = 'home'),
    path('register/', views.registerUser, name = 'register'),
    path('login/', views.loginUser, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),

]