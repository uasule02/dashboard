from django.contrib import admin
from .models import UploadedFile, Sector, Year, Month, CustomUser, ReportUpload


# Register your models here.
@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'sector', 'month', 'user', 'file', 'uploaded_at')

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'acronyms', 'id', 'logo')


class YearAdmin(admin.ModelAdmin):
    list_display = ('year_number',)

@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    list_display = ('month_name','year', 'status')  # Use get_month_name_display to display the month name from choices

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ( 'email', 'first_name', 'last_name', 'user_sector', 'is_staff')

@admin.register(ReportUpload)
class ReportUploadAdmin(admin.ModelAdmin):
    list_display = ('id','month', 'year', 'status')

admin.site.register(Year, YearAdmin)
