# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                # "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                # "placeholder": "Password",
                "class": "form-control"
            }
        ))
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].label = 'username'
    #     self.fields['password'].label = 'password'

    # def clean(self):
    #     username = self.cleaned_data['username']
    #     password = self.cleaned_data['password']
    #     if not User.objects.filter(username=username).exists():
    #         raise forms.ValidationError(f'User with {username} dont register.')
    #     user = User.objects.filter(username=username).first()
    #     if user:
    #         if not user.check_password(password):
    #             raise forms.ValidationError("Broken password")

    #     return self.cleaned_data

    # class Meta:
    #     model = User
    #     fields = ('username', 'password1', 'password2')


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                # "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                # "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                # "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    # def get_address(self, request):
