from django import forms
from .models import Member
from django.forms.widgets import CheckboxSelectMultiple
from multiselectfield import MultiSelectFormField


class CreateUserForm(forms.ModelForm):

    passwordCheck = forms.CharField(max_length=100)
    # interest = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices)
    # interest = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=, label="관심학교")
    #interest = MultiSelectFormField(choices=Member.INTEREST_SCHOOL, label="관심학교")

    field_order = ['username',
                 'password',
                 'passwordCheck', 
                 'email', 
                 'school', 
                 'major', 
                 'schoolId', 
                 'imgOfIdcard', 
                 'interest']
    
    class Meta:
        model = Member
        fields = [
            'username',
            'password',
            'email',
            'school',
            'major',
            'schoolId',
            'imgOfIdcard',
            'interest']

        widgets = {
            'email': forms.EmailInput(
                attrs={
                  #  'class': 'form-control',
                    'placeholder': 'Email',
                    'name': 'email',
                    'id': 'email',
                    'type': 'text',
                }),
            'username': forms.TextInput(
                attrs={
                  #  'class': 'form-control',
                    'placeholder': 'Name',
                    'name': 'name',
                    'id': 'name',
                    'type': 'text',
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'password',
                    'name': 'password',
                    'placeholder': 'Password',
                }),
            'passwordCheck': forms.PasswordInput(
                attrs={
                    'class': 'password2',
                    'id': 'password2',
                    'placeholder': 'Password',
                }),


            'school': forms.Select(
                attrs={
                    'type': 'radio',
                    #  'name': 'r1',
                    #  'id': 'r1',
                }),
            'major': forms.TextInput(
                attrs={
                    'name': 'schoolMajor',
                    'type': 'text',
                    'id': 'schoolMajor',
                    'placeholder': '전공',
                }),
        
            'schoolId': forms.TextInput(
                attrs={
                    'type': 'text',
                    'name': 'schoolId',
                    'id': 'schoolId',
                    'placeholder': "학번",
                }),
            'imgOfIdcard': forms.FileInput(
                attrs={
                    'type': 'file',
                    'name': 'imgOfcard',
                    'id': 'imgOfcard',
                    'accept': '.jpg, .png'
                }),
            'interest': forms.CheckboxSelectMultiple(
                attrs={
                    'type': 'checkbox',
                }),
            
        }

        # queryset = {
        #     'interest': InterestSchool.objects.all()
        # }

        choices = {
            'interest': Member.INTEREST_SCHOOL,
        }

        labels = {
            'username' : 'ID',
            'password' : 'PW',
            'email' : '이메일',
            'school' : '대학교',
            'major' : '학과(주전공)',
            'schoolId' : '학번',
            'imgOfIdcard' : '학생증 사진',
            'interest': '관심 학교',
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15
        self.fields['interest'] = MultiSelectFormField(choices=Member.INTEREST_SCHOOL, label="관심학교")
        



class LoginForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'input100',
                    'type': 'text',
                    'name': 'username',
                }),

            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'class': 'input100',
                    'type': 'password',
                    'name': 'password',
                }),
        }

class DeleteAccountForm(forms.Form):
    username = forms.CharField()

class ChangePasswordForm(forms.Form):
    currentPassword = forms.CharField(max_length=100, widget=forms.PasswordInput())
    newPassword = forms.CharField(max_length=100, widget=forms.PasswordInput())
    newPasswordCheck = forms.CharField(max_length=100, widget=forms.PasswordInput())