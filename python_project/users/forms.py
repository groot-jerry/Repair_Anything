
from django import forms

from users.models import UserProfile


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'user',
            'role',
        ]
