from django import forms
from .models import Hospital_center

class Hospital_centerForm(forms.ModelForm):
    class Meta:
        model = Hospital_center
        fields = '__all__'
