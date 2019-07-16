from django import forms
from .models import SchoolReview
import datetime

class SchoolReviewForm(forms.ModelForm):
    class Meta:
        model = SchoolReview
        fields = ['school', 'content', 'date'] 

        widgets = {
            'school': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'value': '학교명',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '5',
                }
            ),
            'date': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type':'date',
                }
            )
        }