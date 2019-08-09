from django import forms
from .models import SchoolReview
import datetime

class SchoolReviewForm(forms.ModelForm):
    class Meta:
        model = SchoolReview
        fields = ['school', 'schoolyear', 'schoolsemester', 'content'] 

        labels = {
            'school' : '학교명',
            'schoolyear' : '수강년도',
            'schoolsemester' : '수강학기',
        }

        widgets = {
            'school': forms.Select(
            attrs={
                'class': 'field',
                'id': 'select',
                'name': 'select',
            }),
            'schoolyear': forms.Select(
            attrs={
                'class': 'field',
                'id': 'select',
                'name': 'select',
            }),
            'schoolsemester': forms.Select(
            attrs={
                'class': 'field',
                'id': 'select',
                'name': 'select',
            }),     
            'content': forms.Textarea(
            attrs={
                'class': 'field',
                'id': 'textarea',
                'name': 'textarea',
            }),

        }