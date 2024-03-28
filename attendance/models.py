from django.db import models

class FaceRegistration(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='faces/')
    # Add any additional fields as needed

    def __str__(self):
        return self.name
