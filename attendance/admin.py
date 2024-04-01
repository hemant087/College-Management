from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .models import Student

# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username','user_type']

admin.site.register(FaceRegistration)