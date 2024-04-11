from django import forms
from .models import Tertiary_center

class Tertiary_centerForm(forms.ModelForm):
    class Meta:
        model = Tertiary_center
        fields = '__all__'
