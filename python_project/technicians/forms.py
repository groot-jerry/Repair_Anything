
from django import forms

from technicians.models import Technician


class TechnicianCreationForm(forms.ModelForm):
    class Meta:
        model = Technician
        fields = [
            'user',
            'skills',
        ]
