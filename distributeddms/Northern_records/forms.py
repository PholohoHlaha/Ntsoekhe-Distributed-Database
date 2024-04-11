from django import forms
from .models import PatientRecord

class PatientRecordForm(forms.ModelForm):
    class Meta:
        model = PatientRecord
        fields = '__all__'
