from django.shortcuts import render, redirect, HttpResponse
from attendance.form import FaceRegistrationForm
from attendance.models import FaceRegistration
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime


def ATTENDANCE(request):
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date')
        selected_date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
        formatted_date = selected_date_obj.strftime('%Y-%m-%d')

        attendance_data = FaceRegistration.objects.filter(
            date=formatted_date).values_list('name', 'time')

        if not attendance_data:
            return render(request, 'Attendance/attendance.html', {'selected_date': selected_date, 'no_data': True})

        return render(request, 'Attendance/attendance.html', {'selected_date': selected_date, 'attendance_data': attendance_data})

    return render(request, 'Attendance/attendance.html', {'selected_date': '', 'no_data': False})


def ATTENDANCE_SHEET(request):
    return render(request, 'Attendance/attendance_sheet.html')


def register_face(request):
    if request.method == 'POST':
        form = FaceRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page
            return redirect('registration_success')
    else:
        form = FaceRegistrationForm()
    return render(request, 'Attendance/register_face.html', {'form': form})


def registration_success(request):
    return render(request, 'Attendance/registration_success.html')


def face_list(request):
    faces = FaceRegistration.objects.all()
    return render(request, 'Attendance/face_list.html', {'faces': faces})


def face_detail(request, face_id):
    face = FaceRegistration.objects.get(id=face_id)
    return render(request, 'faceregistration/face_detail.html', {'face': face})


def delete_face(request, face_id):
    face = FaceRegistration.objects.get(id=face_id)
    face.delete()
    return redirect('face_list')  # Redirect to the face list page
