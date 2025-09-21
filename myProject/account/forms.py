from django import forms
from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class UserSearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=100)