from django import forms
from django.contrib.auth.models import User
from third_app.models import UserProfileInfo,Comment

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('profile_pics','age','phone_no')

class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('content',)
