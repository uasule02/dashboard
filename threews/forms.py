# forms.py
from django import forms

from .models import UploadedFile, Month, Year

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
        time = ['uploaded_at']
        
class MonthFilterForm(forms.Form):
    year = forms.ModelChoiceField(
        queryset=Year.objects.all(),
        empty_label="Select a Year",
        required=False
    )