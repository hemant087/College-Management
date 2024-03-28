from django import forms
from .models import FaceRegistration

class FaceRegistrationForm(forms.ModelForm):
    class Meta:
        model = FaceRegistration
        fields = ['name', 'image']  # Include other fields if needed
