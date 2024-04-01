from django.db import models

class FaceRegistration(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='faces/')
    # Add any additional fields as needed
    class Meta:
        app_label = 'attendance'

    def __str__(self):
        return self.name
