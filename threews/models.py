from django.db import models

# Create your models here.


class UploadedFile(models.Model):
    #sector = 
    #quater =
    #year =
    #user =
    file = models.FileField(upload_to= 'upload/3ws')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Sector(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    acronyms = models.CharField(max_length=50, blank=False, null=False)    
    logo = models.FileField(upload_to='assets/media/svg/brand-logos', null=True, blank=True)  



    def __str__(self):
        return self.name
    
