from django.contrib import admin
from Blogs import views
from django.urls import path,include

urlpatterns=[
    path('blogs/',views.blogs,name="blogs"), #Blogs page url
    path('blog/<slug:slug>',views.blog,name="blog"), #blog filtered by slug url
    path('dashboard/',views.dashboard,name="dashboard"), #dashbaord url
    path('AddBlog/',views.AddBlog,name="AddBlog"), #add blog url
    path('UpdateBlog/<slug:slug>',views.UpdateBlog,name="UpdateBlog"), #Update blog url
    path('DeleteBlog/<slug:slug>',views.DeleteBlog,name="DeleteBlog") #Delete blog url(this url it is only used delete blogs and not running any html template)
]