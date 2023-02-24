from django import forms
from core.models import User


class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
