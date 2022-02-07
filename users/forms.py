import email
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegisterForm(UserCreationForm):
    # field to be added in the form
    email=forms.EmailField()
    class Meta:
        model = User
        # Fields we want on the form
        fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    # field to be added in the form
    email=forms.EmailField()
    class Meta:
        model = User
        # Fields we want on the form
        fields=['username','email']
class ProfileUpdateForm(forms.ModelForm):
    # field to be added in the form
    class Meta:
        model = Profile
        # Fields we want on the form
        fields=['image']