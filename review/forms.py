from django import forms
from .models import Review

class ReviewForm(forms.ModelForm) :
    class Meta :
        model = Review
        fields = ['univ', 'coursename', 'prof', 'courseyear', 'coursesemester', 'content', 'assignment', 'test', 'attendence', 'star']

        labels = {
            'univ' : '대학교',
            'coursename' : '강의명',
            'prof' : '교수',
            'courseyear' : '수강년도',
            'coursesemester' : '수강학기',
            'content' : '강의평',
            'assignment' : '과제',
            'test' : '시험',
            'attendence' : '출결',
            'star' : '별점',
        }
        widgets = {
            'star': forms.RadioSelect,
            }