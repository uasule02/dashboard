from django.contrib import admin
from .models import UploadedFile, Sector


# Register your models here.
@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'acronyms', 'id', 'logo')
