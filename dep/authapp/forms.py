from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authapp.models import DepUser


class LoginForm(AuthenticationForm):
    class Meta:
        model = DepUser
        fields = (
            'login',
            'password'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control mt-2'
            item.help_text = ''


class RegisterForm(UserCreationForm):

    class Meta:
        model = DepUser
        fields = (
            'login',
            'password1',
            'password2',
            'name',
            'surname',
            'email',
            'patronymic',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name}'
            item.help_text = ''
