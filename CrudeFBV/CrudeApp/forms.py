from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import Student
from django.core import validators

class studentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'role':forms.TextInput(attrs={'class':'form-control'}),
        }
