# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from app.models import Course, Session_Year, Student
# from app.models import CustomUser


# @login_required(login_url='/')
# def HOME(request):
#     return render(request, 'Hod/home.html')


# @login_required(login_url='/')
# def ADD_STUDENT(request):
#     course = Course.objects.all()
#     session_year = Session_Year.objects.all()

#     if request.method == "POST":
#         username = request.POST.get('username')
#         profile_pic = request.FILES.get('profile_pic')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         mobile_number = request.POST.get('mobile_number')
#         registration = request.POST.get('registration')
#         roll = request.POST.get('roll')
#         course_id = request.POST.get('course_id')
#         session_year_id = request.POST.get('session_year_id')
#         gender = request.POST.get('gender')
#         dob = request.POST.get('dob')
#         password = request.POST.get('password')
#         address = request.POST.get('address')

#         print(username, profile_pic, password, first_name, last_name, email, mobile_number,
#               registration, roll, course_id, session_year_id, gender, dob, address)

#         if CustomUser.objects.filter(email=email).exists():
#             messages = Warning(request, 'Email is Already Exists')
#             return redirect('add_student')
#         if CustomUser.objects.filter(username=username).exists():
#             messages = Warning(request, 'Username is Already Exists')
#             return redirect('add_student')
#         else:
#             user = CustomUser(
#                 first_name=first_name,
#                 last_name=last_name,
#                 username=username,
#                 email=email,
#                 profile_pic=profile_pic,
#                 user_type=3
#             )
#             user.set_password(password)
#             user.save()
#             course = Course.objects.get(id=course_id)
#             session_year = Session_Year.objects.get(id=session_year_id)
#             student = Student(
#                 admin=user,
#                 address=address,
#                 session_year_id=session_year,
#                 course_id=course,
#                 gender=gender,
#                 roll=roll,
#                 registration=registration,
#                 mobile_number=mobile_number,
#                 dob=dob,
#             )

#             student.save()
#             messages.success(request, user.first_name + "  " +
#                              user.last_name + " has been successfully added!")
#             return redirect('add_student')
#     context = {
#         'course': course,
#         'session_year': session_year
#     }

#     return render(request, 'Hod/add_student.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Course, Session_Year, Student
from app.models import CustomUser
from django.db import IntegrityError


@login_required(login_url='/')
def HOME(request):
    return render(request, 'Hod/home.html')


@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        username = request.POST.get('username')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        registration = request.POST.get('registration')
        roll = request.POST.get('roll')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists!')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists!')
            return redirect('add_student')
        else:
            try:
                # Your existing code to save the user and student records...
                user = CustomUser(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    profile_pic=profile_pic,
                    user_type=3
                )
                user.set_password(password)
                user.save()
            except IntegrityError:
                messages.error(request, 'Registration number already exists!')
                return redirect('add_student')

        # If both email and username are unique, proceed to create user and student

        # Get course and session year objects
        course_obj = Course.objects.get(id=course_id)
        session_year_obj = Session_Year.objects.get(id=session_year_id)

        # Create student object
        student = Student(
            admin=user,
            address=address,
            session_year=session_year_obj,
            course=course_obj,
            gender=gender,
            roll=roll,
            registration=registration,
            mobile_number=mobile_number,
            dob=dob,
        )
        student.save()

        messages.success(
            request, f'{user.first_name} {user.last_name} has been successfully added!')
        return redirect('add_student')

    context = {
        'course': course,
        'session_year': session_year
    }

    return render(request, 'Hod/add_student.html', context)
