from django import forms
from .models import Member


class CreateUserForm(forms.ModelForm):
    passwordCheck = forms.CharField(max_length=100, widget=forms.PasswordInput())

    field_order = ['username', 'password', 'passwordCheck', 'school', 'major', 'schoolId', 'imgOfIdcard']
    
    class Meta:
        model = Member
        fields = [
            'username',
            'password',
            'school',
            'major',
            'schoolId',
            'imgOfIdcard']

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '15자 이내로 입력 가능합니다.'
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                }),
        }

        labels = {
            'username' : '아이디',
            'password' : '패스워드',
            'school' : '학교',
            'major' : '학과(주전공)',
            'schoolId' : '학번',
            'imgOfIdcard' : '학생증 사진',
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15

class LoginForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'password']

        widgets = {
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                }),
        }

class DeleteAccountForm(forms.Form):
    username = forms.CharField()