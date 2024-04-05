from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Course, Session_Year, Student, Teacher
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


def VIEW_STUDENT(request):
    student = Student.objects.all()

    context = {
        'student': student,
    }

    return render(request, 'Hod/view_students.html', context)


@login_required(login_url='/')
def EDIT_STUDENT(request, id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    context = {
        'student': student,
        'course': course,
        'session_year': session_year,
    }
    return render(request, 'Hod/edit_student.html', context)


@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        print(student_id)
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

        user = CustomUser.objects.get(id=student_id)

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password != 'None' and password != "":
            user.set_password(password)
        if password != 'None' and password != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id=course_id)
        student.course_id = course

        session_year = Session_Year.objects.get(id=session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request, 'Record has been successfully updated!')
        return redirect('view_student')

    return render(request, 'Hod/edit_student.html')


def DELETE_STUDENT(request, admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request, "Record has been successfully deleted")
    return redirect('view_student')


def ADD_DEPARTMENT(request):
    if request.method == "POST":
        dept_name = request.POST.get('dept_name')
        dept_id = request.POST.get('dept_id')
        dept_hod = request.POST.get('dept_hod')
        start_date = request.POST.get('start_date')
        num_student = request.POST.get('num_student')

        # Validate the form data (e.g., check if required fields are not empty)

        if Course.objects.filter(dept_name=dept_name).exists():
            messages.warning(request, 'Department already exists!')
        else:
            # Create a new department object and save it to the database
            dept = Course(
                dept_name=dept_name,
                dept_id=dept_id,
                dept_hod=dept_hod,
                start_date=start_date,
                num_student=num_student
            )
            dept.save()
            messages.success(
                request, f'{dept.dept_name} has been successfully added!')
        # return render(request, 'Hod/add_department.html')
        return redirect('add_department')
    return render(request, 'Hod/add_department.html')


def VIEW_DEPARTMENT(request):
    department = Course.objects.all()

    context = {
        'department': department,
    }

    return render(request, 'Hod/view_department.html', context)


def EDIT_DEPARTMENT(request, id):
    course = Course.objects.filter(id=id)

    context = {
        'course': course,
    }
    return render(request, 'Hod/edit_department.html', context)


def UPDATE_DEPARTMENT(request):
    if request.method == "POST":
        id = request.POST.get('id')
        dept_name = request.POST.get('dept_name')
        dept_id = request.POST.get('dept_id')
        dept_hod = request.POST.get('dept_hod')
        start_date = request.POST.get('start_date')
        num_student = request.POST.get('num_student')
        print(id, dept_hod)

        # Retrieve the Course object based on dept_id
        course = Course.objects.get(id=id)

        # Update the department details
        course.dept_id = dept_id
        course.dept_name = dept_name
        course.dept_hod = dept_hod
        course.num_student = num_student

        # Save the changes
        course.save()

        # Add a success message
        messages.success(request, 'Record has been successfully updated!')

        # Redirect to a different URL after successful submission
        return redirect('view_department')

    return render(request, 'Hod/edit_department.html')


def DELETE_DEPARTMENT(request, id):
    dept = Course.objects.get(id=id)
    dept.delete()
    messages.success(request, "Department has been successfully deleted")
    return redirect('view_department')


# ----------------------TEACHER---------------------------


@login_required(login_url='/')
def ADD_TEACHER(request):

    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        address = request.POST.get('address')
        Qualification = request.POST.get('Qualification')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists!')
            return redirect('add_teacher')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists!')
            return redirect('add_teacher')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                user_type=2
            )
            user.set_password(password)
            user.save()

        # Create teacher object
        teacher = Teacher(
            admin=user,
            address=address,
            gender=gender,
            mobile_number=mobile_number,
            Qualification=Qualification,
        )
        teacher.save()

        messages.success(
            request, f'{user.first_name} {user.last_name} has been successfully added!')
        return redirect('add_teacher')
    return render(request, 'Teacher/add_teacher.html')


def VIEW_TEACHER(request):
    teacher = Teacher.objects.all()
    context = {
        'teacher': teacher,
    }
    return render(request, 'Teacher/view_teacher.html', context)


@login_required(login_url='/')
def EDIT_TEACHER(request):
    teacher = Teacher.objects.all()
    context = {
        'teacher': teacher,
    }
    return render(request, 'Teacher/edit_teacher.html', context)


@login_required(login_url='/')
def UPDATE_TEACHER(request):
    if request.method == "POST":
        teacher_id = request.POST.get('teacher_id')
        username = request.POST.get('username')
        # profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        address = request.POST.get('address')
        city = request.POST.get('address')
        state = request.POST.get('address')

        user = CustomUser.objects.get(id=teacher_id)

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password != 'None' and password != "":
            user.set_password(password)
        # if password != 'None' and password != "":
        #     user.profile_pic = profile_pic
        user.save()

        teacher = Student.objects.get(admin=teacher_id)
        teacher.address = address
        teacher.gender = gender
        teacher.save()

        messages.success(request, 'Record has been successfully updated!')
        return redirect('view_teacher')
    return render(request, 'Teacher/edit_teacher.html')


def DELETE_TEACHER(request, admin):
    teacher = CustomUser.objects.get(id=admin)
    teacher.delete()
    messages.success(request, "Record has been successfully deleted")
    return redirect('delete_teacher')
    # return render(request, 'Teacher/view_teacher.html')
