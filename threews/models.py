from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission



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
    def __str__(self):
        return f"{self.month_name} - {self.year}"
    
class ReportUpload(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    sectors = models.ManyToManyField(Sector)
    status_choices = [('open', 'Open'), ('closed', 'Closed')]
    status = models.CharField(max_length=10, choices=status_choices)

    def __str__(self):
        return f"{self.month} - {self.year} -  {self.status}"



class UploadedFile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE,null=True, blank=True)
    month = models.ForeignKey(ReportUpload,  on_delete=models.CASCADE,null=True, blank=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=255, editable=False) 
    file = models.FileField(upload_to= 'upload/3ws')
    uploaded_at = models.DateTimeField(auto_now_add=True)
     # Add the 'name' field

    def save(self, *args, **kwargs):
        # Create the name using the sector, month, and year fields
        name = f"{self.sector.acronyms} - {self.month.month}"

        # Assign the generated name to the name field
        self.name = name

        # Call the original save method
        super().save(*args, **kwargs)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    user_sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Specify a unique related_name for groups and user_permissions fields
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',  # Change this to a unique name
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',  # Change this to a unique name
        related_query_name='user',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    



