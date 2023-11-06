from django.contrib import admin
from .models import UploadedFile, Sector, Year, Month


# Register your models here.
@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'acronyms', 'id', 'logo')


class YearAdmin(admin.ModelAdmin):
    list_display = ('year_number',)

@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    list_display = ('month_name','year', 'status')  # Use get_month_name_display to display the month name from choices



admin.site.register(Year, YearAdmin)
