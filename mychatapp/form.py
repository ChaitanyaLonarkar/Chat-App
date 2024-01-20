# your_app/forms.py
from django import forms
from .models import Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username','first_name', 'last_name', 'profile_picture']
