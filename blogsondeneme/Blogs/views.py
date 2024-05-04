from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from .forms import BlogForm
from django.core.paginator import Paginator
from django.contrib import messages

def index(request): #Homepage code
    return render(request,"index.html")

def blogs(request): #Function written to show all blogs on the blog page
    keyword = request.GET.get("keyword")#This line is used to retrieve the information entered into the search input field on the blogs page.

    if keyword: #In this control, after filtering the information from the keyword variable based on the title information of the blog, we send the filtered blogs to the blogs page.
        blogs = Blog.objects.filter(title__contains = keyword)
        return render(request,"blogs.html",{"blogs":blogs})
    blogs = Blog.objects.all() #This line retrieves all the blogs from the Blog model.
    
    context = { #We are sending the blogs we obtained from the 'blogs' variable to 'blogs.html using the context.
        "blogs":blogs
    }

    return render(request,"blogs.html",context)

def blog(request,slug): #Function that shows blogs filtered by slug
    blog = Blog.objects.get(slug=slug) #This line filters the blogs from the Blog model based on their slug.
    context = { #This line sends the filtered blog obtained from the 'blog' variable to 'blog.html' using the context.
        "blog":blog
    }
    return render(request,"blog.html",context)

def dashboard(request): #The function created for users to view their own blogs
    keyword = request.GET.get("keyword") #This line retrieves the 'keyword' information from the search input on the dashboard page using the 'keyword' variable.

    if keyword: #With this control, we filter the information coming from the keyword and the title of the blog obtained from the 'blogs' variable, and then send it to the dashboard page
        blogs = Blog.objects.filter(title__contains = keyword)
        return render(request,"dashboard.html",{"blogs":blogs})
    blogs = Blog.objects.all()

    blogs = Blog.objects.filter(author = request.user) #This line filters the blogs based on the user who is currently logged in.

    context = { #Here, it sends the information obtained from the 'blogs' variable to the 'dashboard.html' page using the context variable.
        "blogs":blogs
    }
    return render(request,"dashboard.html",context)

def AddBlog(request): #The function enabling the user to add a blog.
    form = BlogForm(request.POST or None,request.FILES or None) #With this 'form' variable, we are obtaining the BlogForm form from forms.py.
    if form.is_valid(): #Here, if the form is validated, we first defer the form submission, match the author of our blog with the logged-in user, then save our form and notify the user with a message
        blog = form.save(commit=False) #We are deferring the form.

        blog.author = request.user #We are matching the author with the logged-in user.
        blog.save() #We are saving the blog.

        messages.success(request,'Blog Added Successfully')
        return redirect("dashboard")
    else:
        messages.error(request,form.errors) #
    return render(request,"AddBlog.html",{"form":form})

def UpdateBlog(request,slug): #The function allowing the user to make changes to the blog.
    blog = get_object_or_404(Blog,slug=slug) #This line retrieves the blogs from the Blog model based on their slug using the 'blog' variable.
    form = BlogForm(request.POST or None,request.FILES or None,instance = blog) #With this line, we are obtaining the BlogForm from the form variable

    if form.is_valid(): #Here, if the form is validated, we are deferring the saving of the form with the blog variable, then matching the author of the blog with the logged-in user, and finally saving our form.
        blog = form.save(commit=False) #We are deferring the saving of the form.

        blog.author = request.user #We are matching the author of the blog with the logged-in user.
        blog.save() #We are saving our form

        messages.success(request,'Blog Editing Successfully')
        return redirect("dashboard")
    else:
        messages.error(request,form.errors)

    return render(request,"UpdateBlog.html",{"form":form})

def DeleteBlog(request,slug): #The function created for users to delete their blogs
    blog = get_object_or_404(Blog,slug=slug) #We are retrieving our blog from the Blog model based on its slug.
    blog.delete() #We are deleting our form

    messages.success(request,"Blog deleted successfully")
    return redirect("dashboard")

