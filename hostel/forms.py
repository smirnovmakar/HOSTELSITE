from .models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'email', 'password']
        widgets = {
            'user_name': TextInput(attrs={
                "type": "text",
            }),
            'email': EmailInput(attrs={
                "type": "email",
            }),
            'password': PasswordInput(attrs={
                "type": "password",
                "minlength": 6
            })
        }
