from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser,Attendance
from datetime import datetime


def BASE(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request, username=request.POST.get(
            'email'), password=request.POST.get('password'),)
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return HttpResponse('This is staff Penal')
            elif user_type == '3':
                return HttpResponse('This is student Penal')
            else:
                messages.error(request, "Email and Password are invalid")
                return redirect('login')

        else:
            messages.error(request, "Email and Password are invalid")
            return redirect('login')


def doLogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        'user': user
    }
    return render(request, 'profile.html')


@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        try:
            customUser = CustomUser.objects.get(id=request.user.id)
            customUser.first_name = first_name
            customUser.last_name = last_name

            if password != 'None' and password != "":
                customUser.set_password(password)
            if password != 'None' and password != "":
                customUser.profile_pic = profile_pic
            customUser.save()
            messages.success(request, "Your profile Updated Successfully ! ")
            return redirect('profile')
        except:
            messages.error(request, 'Failed to Update your Profile')
    return render(request, "profile.html")

def ATTENDANCE(request):
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date')
        selected_date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
        formatted_date = selected_date_obj.strftime('%Y-%m-%d')

        attendance_data = Attendance.objects.filter(date=formatted_date).values_list('name', 'time')

        if not attendance_data:
            return render(request, 'Attendance.html', {'selected_date': selected_date, 'no_data': True})
        
        return render(request, 'Attendance.html', {'selected_date': selected_date, 'attendance_data': attendance_data})

    return render(request, 'Attendance.html', {'selected_date': '', 'no_data': False})
