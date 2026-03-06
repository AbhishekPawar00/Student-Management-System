from django import forms
from .models import Student
from django.contrib.auth.models import User
import re

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

    def clean_full_name(self):
        name = self.cleaned_data['full_name']
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name should not contain numbers")
        return name

    def clean_phone(self):
        phone = str(self.cleaned_data.get('phone'))
        if not re.fullmatch(r'\d{10}', phone):
            raise forms.ValidationError("Phone must be 10 digits")
        return phone


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']