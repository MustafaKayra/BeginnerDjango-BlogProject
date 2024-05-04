from django.db import models
from django.utils.text import slugify

class Blog(models.Model): #Blog Model
    title = models.CharField(max_length = 200,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    is_active = models.BooleanField(default = True)
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True)
    image = models.ImageField(upload_to="blogsondeneme\Blogs\static\img")

    def __str__(self): #To make blogs appear with their titles on the admin page
        return f"{self.title}"
    
    def save(self, *args, **kwargs): #This function adds slug by title
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    

