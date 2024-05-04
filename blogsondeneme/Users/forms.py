from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages

class RegisterForm(UserCreationForm): #Register Form
    username = forms.CharField(label="username", min_length=0, max_length=50, required=True) #username information and validators
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, max_length=20,required=True) #password information and validators
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, max_length=20,required=True) #confirm password
    email = forms.EmailField(max_length=256, min_length=0, required=True) #email information and validators
    first_name = forms.CharField(max_length=20,min_length=3,required=False) #first name information and validators
    last_name = forms.CharField(max_length=10,min_length=3,required=False) #last name and validators

    def clean(self): #I wrote this function to validate the password entered by the user
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1") #We are retrieving the 'password1' information from the form
        password2 = cleaned_data.get("password2") #We are retrieving the 'password2' information from the form

        if password1 != password2: #If 'password1' is not equal to 'password2', we give the error message to the user
            raise ValidationError("password do not match!")
        
        return cleaned_data
    

    class Meta: #This class specifies which model the RegisterForm uses and defines its fields.
        model = User #User model
        fields = ('username','password1','password2','email','first_name','last_name') #Register form fields

class LoginForm(forms.Form): #Login form
    username = forms.CharField(label="Username") #get a username information
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput) #get a password information

class UpdateUserTestForm(forms.Form): #Update User Form
    password1 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput,required=True) #Password information and validators
