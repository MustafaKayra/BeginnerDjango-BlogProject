from django.contrib import admin
from django.urls import path,include
from Users import views

urlpatterns = [
    path('register/',views.register,name="register"), #Register page url
    path('login/',views.loginUser,name = "login"), #Login page url
    path('logout/',views.logoutUser,name="logout"), #logout url(this url it is only used logout and not running any html template)
    path('UpdateUser/<int:id>',views.UpdateUser,name="UpdateUser"), #Update user page url
    path('profile/',views.profile,name="profile") #profile page url
]