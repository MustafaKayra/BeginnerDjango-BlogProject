from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages



def register(request): #This function enables the user to register.
    if request.method == 'POST': #We are checking our request method.
        form = RegisterForm(request.POST) #We are obtaining our RegisterForm with the form variable
        if form.is_valid(): #If our form is validated, we proceed with the operations.
            username = form.cleaned_data.get("username") #We are retrieving the 'username' information from our form.
            raw_password = form.cleaned_data.get("password1") #We are retrieving the 'password1' information from our form.
            email = form.cleaned_data.get("email") #We are retrieving the 'email' information from our form.
            first_name = form.cleaned_data.get("first_name") #We are retrieving the 'first_name' information from our form.
            last_name = form.cleaned_data.get("last_name") #We are retrieving the 'last_name' information from our form.

            hashed_password = make_password(raw_password) #In this line, we use 'make_password' to hash the 'password1' information obtained with the 'raw_password' variable.
            newUser = User.objects.create(username=username,email=email,password=hashed_password,first_name=first_name,last_name=last_name) #We are using the information from the form submitted by the user in the 'newUser' variable and saving it to the database.
            newUser.save() #We are saving User
            
            login(request,newUser) #We are logging in the user.

            messages.success(request,'registered and logged in successfully')
            return redirect('index')
        else:
            messages.warning(request,'You made a mistake in your form, please try again.')
        
    else:
        print('There is an error!')
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def loginUser(request): #This function enables the user to log in.
    form = LoginForm(request.POST) #We are obtaining our RegisterForm with the form variable
    if request.method == 'POST': #We are checking our request method.
        if form.is_valid():
            username = form.cleaned_data.get("username") #We are retrieving the 'username' information from our form.
            password = form.cleaned_data.get("password1") #We are retrieving the 'password1' information from our form.

            user = authenticate(username=username,password=password) #We are checking if such a session exists using the 'user' variable and the 'authenticate' function
            if user is not None: #If there is a session that matches the information provided to the 'authenticate' function
                messages.success(request,'Logged in successfully')
                login(request,user) #We are logging in the user.
                return redirect('index')
            else:
                messages.warning(request,'username or password is wrong')
        else:
            print('YİNE FORMDA SIKINTI VAR')
            messages.error(request,form.errors)
    else:
        form = LoginForm()
    return render(request,"login.html",{"form":form})

def logoutUser(request): #This function enables the user to logout
    logout(request) #We are logging out the user.
    messages.success(request,'Successfully logged out')
    return redirect('index')

def UpdateUser(request,id):#This function is used to update the user's information.
    user = get_object_or_404(User,id=id) #This line retrieves users based on their IDs using the 'user' variable.
    form = RegisterForm(request.POST or None,instance=user) #We are obtaining the RegisterForm with the 'form' variable (we will use RegisterForm for user updates)
    context = { #We are sending our form to the 'UpdateUser.html' page using the context
        "form":form
    }
    if form.is_valid(): #If our form is validated, we proceed with the operations.
        form.save() #We are saving our form
        password1 = form.cleaned_data.get("password1") #We are retrieving the 'password1' information from the form using the 'password1' variable.

        updated_user = authenticate(username = user.username,password = password1) #We are checking if there is a session matching the 'username' and 'password1' using the 'updated_user' variable and the 'authenticate' function.

        if updated_user is not None: #If there is a session verified by the authentication process
            login(request,updated_user) #We are logging in the user
            messages.success(request,'User updated successfully and logged')
            return redirect('profile')
        else:
            messages.warning(request,'There is a problem with logging in.')

    else:
        form = RegisterForm()
        print('akilsagliginikaybet.')
    
    return render(request,"UpdateUser.html",context)

            
def profile(request): #This function enabled to user looking own profile.
    profile = User.objects.filter(username=request.user) #We are filtering users from the User model based on the session they have opened using the 'profile' variable.
    
    context = { #We are sending the 'profile' variable to the 'profile.html' page using the context.
        "profile":profile
    }

    return render(request,"profile.html",context)