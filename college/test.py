from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from app.models import CustomUser, Course, Session_Year, Student

@login_required(login_url='/')
def ADD_STUDENT(request):
    courses = Course.objects.all()
    session_years = Session_Year.objects.all()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
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
        profile_pic = request.FILES.get('profile_pic')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email is Already Exists')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username is Already Exists')
            return redirect('add_student')
        else:
            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            course_obj = Course.objects.get(id=course_id)
            session_year_obj = Session_Year.objects.get(id=session_year_id)
            student = Student.objects.create(
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
            messages.success(request, f"{user.first_name} {user.last_name} has been successfully added!")
            return redirect('add_student')  # Redirect to the same page or a different page

    context = {
        'courses': courses,
        'session_years': session_years
    }
    return render(request, 'add_student.html', context)
