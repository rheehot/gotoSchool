from django import forms
from .models import Review

class ReviewForm(forms.ModelForm) :
    class Meta :
        model = Review
        fields = ['univ', 'coursename', 'prof', 'courseyear', 'coursesemester', 'content', 'assignment', 'test', 'attendence', 'star']

        labels = {
            'univ' : '대학교',
            'coursename' : '강의명', #text
            'prof' : '교수', #text
            'courseyear' : '수강년도',
            'coursesemester' : '수강학기',
            'content' : '강의평', #textarea
            'assignment' : '과제',
            'test' : '시험',
            'attendence' : '출결',
            'star' : '별점', #radio
        }
        widgets = {
            'star': forms.RadioSelect(
            attrs={
                'type': 'radio',
                'id': 'radio1',
                'name': 'radio',
            }),
            'content': forms.Textarea(
            attrs={
                'class': 'field',
                'id': 'textarea',
                'name': 'textarea',
            }),
            'coursename': forms.TextInput(
            attrs={
                'type': 'text',
                'id': 'input',
                'name': 'input',
                'class': 'field',
            }),
            'prof': forms.TextInput(
            attrs={
                'type': 'text',
                'id': 'input',
                'name': 'input',
                'class': 'field',
            }),
            'univ': forms.Select(
            attrs={
                'class': 'field',
                'id': 'select',
                'name': 'select',
            }), 
            'courseyear': forms.Select(
            attrs={
                'class': 'field',
                'id': 'select',
                'name': 'select',
            }),
            'coursesemester': forms.Select(
            attrs={
                'class': 'field',
                'id': 'select',
                'name': 'select',
            }),      
            'assignment': forms.Select(
            attrs={
                'class': 'field',
                'id': 'select',
                'name': 'select',
            }),
            'attendence': forms.Select(
            attrs={
                'class': 'field',
                'id': 'select',
                'name': 'select',
            }),
            'test': forms.Select(
            attrs={
                'class': 'field',
                'id': 'select',
                'name': 'select',
            }),


        
        }


