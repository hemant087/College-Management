from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT')
    )

    user_type = models.CharField(choices = USER,max_length = 50, default = 1 )
    profile_pic = models.ImageField(upload_to = 'media/profile_pic', null=True, blank=True)

class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Session_Year(models.Model):
    Session_start = models.CharField(max_length=100)
    Session_end = models.CharField(max_length=100)

class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete= models.CASCADE)