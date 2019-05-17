from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm, SignupForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    signup = SignupForm
    model = CustomUser
    list_display = ['email', 'username', ]

admin.site.register(CustomUser, CustomUserAdmin)
