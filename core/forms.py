from django import forms
from core.models import User, Biens, Depense


class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class AddBienForm(forms.ModelForm):
    class Meta:
        model = Biens
        fields = '__all__'
        exclude = ('user',)


class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = '__all__'
