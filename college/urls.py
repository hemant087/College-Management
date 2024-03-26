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
    path('Hod/Student/View', hod_views.VIEW_STUDENT, name='view_student'),
    path('Hod/Student/Edit/<str:id>', hod_views.EDIT_STUDENT, name='edit_student'),
    path('Hod/Student/Update', hod_views.UPDATE_STUDENT, name='update_student'),
    path('Hod/Student/Delete/<str:admin>',
         hod_views.DELETE_STUDENT, name='delete_student'),

    path('Hod/Department/Add', hod_views.ADD_DEPARTMENT, name='add_department'),
    path('Hod/Department/View', hod_views.VIEW_DEPARTMENT, name='view_department'),
    path('Hod/Department/Edit/<str:id>', hod_views.EDIT_DEPARTMENT, name='edit_department'),
    path('Hod/Department/Update', hod_views.UPDATE_DEPARTMENT, name='update_department'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
