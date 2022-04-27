from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerCreationForm, CustomerUserChangeForm 
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomerCreationForm
    form = CustomerUserChangeForm
    model = CustomUser
    list_display = ['username','email','age','is_staff',]

admin.site.register(CustomUser, CustomUserAdmin)

