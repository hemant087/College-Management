from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    USER = (
        (1, 'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT')
    )

    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(
        upload_to='media/profile_pic', null=True, blank=True)

class Course(models.Model):
    dept_name = models.CharField(max_length=100, unique=True)
    dept_id = models.CharField(max_length=15, unique=True, null=True)
    dept_hod = models.CharField(max_length=100, default="")
    start_date = models.DateField(null=True)
    num_student = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.dept_name



class Session_Year(models.Model):
    semester = models.CharField(max_length=100)
    # Session_end = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.semester


class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    registration = models.IntegerField(max_length=20, unique=True, null=True)
    mobile_number = models.CharField(max_length=20, null=True)
    roll = models.IntegerField(max_length=20, null=True)
    gender = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    session_year = models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.admin.first_name} {self.admin.last_name}"
