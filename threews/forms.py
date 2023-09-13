# forms.py
from django import forms

class YearFilterForm(forms.Form):
    year = forms.ChoiceField(label='Select Year', choices=[])

    def __init__(self, available_years, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'].choices = [(year, year) for year in available_years]
