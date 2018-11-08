from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import validate_email
from .models import Profile

class SignupForm(UserCreationForm):
    pass
    

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='손흥민의 등번호는?')
    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer != 7:
            raise forms.ValidationError('Wrong Answer!')        
        return answer
    