from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'email', 'phone', 'address','school','university','degree',  'experience', 'summary', 'social_link', 'profile_picture']
