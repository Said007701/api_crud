from django import forms
from .models import Gile

class GileForm(forms.ModelForm):
    class Meta:
        model = Gile
        fields = ['name', 'description']