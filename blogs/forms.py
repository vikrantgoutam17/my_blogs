from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#import attr
from django.forms import ModelForm
from .models import blog,user_profile
from ckeditor_uploader.fields import RichTextUploadingField

class PostForm(ModelForm):

    
    class Meta:
        model = blog
        fields = ['title','content','back']
class detailForm(ModelForm):

    class Meta:
        model = user_profile
        fields = ["description","age","country","address","profile_pic","phone_number"]


class NewUserForm(UserCreationForm):
     # declare the fields you will show
    username = forms.CharField(label="Your Username")
    # first password field
    password1 = forms.CharField(label="Your Password",widget=forms.PasswordInput(attrs={'size': '40'}))
    # confirm password field
    password2 = forms.CharField(label="Repeat Your Password",widget=forms.PasswordInput(attrs={'class': 'validate', }))
    email = forms.EmailField(label = "Email Address", )
    first_name = forms.CharField(label = "Name")
    last_name = forms.CharField(label = "Surname")
   
    # this sets the order of the fields
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2",)
 
    # this redefines the save function to include the fields you added 
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
 
        if commit:
            user.save()
        return user
