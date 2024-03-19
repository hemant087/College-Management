from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, hod_views, staff_views, student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # login path
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),

    # profile update
    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),

    # HOD penal
    path('Hod/Home', hod_views.HOME, name='hod_home'),
    path('Hod/Student/Add', hod_views.ADD_STUDENT, name='add_student'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
