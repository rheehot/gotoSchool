from django import forms
from .models import Message
from django.forms import ModelChoiceField
from membership.models import Member

class MessageForm(forms.ModelForm):
    #sender = ModelChoiceField(queryset=Member.objects.all())
    recipient = ModelChoiceField(queryset=Member.objects.all())

    class Meta:
        model = Message
        fields = ['recipient', 'content']

        widgets = {
            'recipient': forms.TextInput(),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '쪽지를 작성해주세요.',
                }
            ),
        }