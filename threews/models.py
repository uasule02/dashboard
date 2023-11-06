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
    

class Year(models.Model):
    year_number = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return str(self.year_number)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            # Automatically create 12 months (Jan to Dec) with status 'closed'
            months = months = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]
            for month_name in months:
                Month.objects.create(year=self, month_name=month_name, status='closed')

class Month(models.Model):
    # Define choices for the month_name field
    MONTH_CHOICES = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]

    # Choices for the status field
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('finished', 'Finished'),
    ]

    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    month_name = models.CharField(max_length=20, choices=MONTH_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='closed')
    

   