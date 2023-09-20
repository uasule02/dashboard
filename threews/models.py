from django.db import models

# Create your models here.


class UploadedFile(models.Model):
    #sector = 
    #quater =
    #year =
    #user =
    file = models.FileField(upload_to= 'upload/3ws')
    uploaded_at = models.DateTimeField(auto_now_add=True)