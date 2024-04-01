from django.urls import path
from . import views

urlpatterns = [
    path('', views.doLogin, name='home'),
    # Other URL patterns...
]
