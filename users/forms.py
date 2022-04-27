from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomerCreationForm(UserCreationForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username','email','age')

class CustomerUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','email','age')
        