from django import forms
from app_ip.models import University, Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'institution', 'year']


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['full_name', 'short_name', 'date']

