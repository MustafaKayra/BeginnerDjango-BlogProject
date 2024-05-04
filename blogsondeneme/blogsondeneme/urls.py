from django.contrib import admin
from django.urls import path,include
from Blogs import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('blogs/',include("Blogs.urls")),
    path('user/',include("Users.urls"))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)