from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_face, name='register_face'),
    # Define other URLs as needed
]
