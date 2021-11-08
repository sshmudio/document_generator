# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# class DocForm(forms.ModelForm):
#     class Meta:
#         model = DocUkraineInternational
#         fields = [
#             'given_name',
#             'surname',
#             'passport_number',
#             'genre',
#             'birth_date',
#             'locations',
#             'photo_doc',
#             'remove_bg',
#             'get_exif_info',
#             'background_image']


# class StateCardUsaForm(forms.ModelForm):
#     class Meta:
#         model = StateCardUsa
#         fields = [
#             'passport_card_number',
#             'nationality',
#             'surname',
#             'given_names',
#             'sex',
#             'date_of_birdth',
#             'place_of_birth',
#             'issues_on',
#             'expiries_on',
#             'documment_id',
#             'photo_document',
#             'remove_bg',
#             'get_exif_info',
#             'background_image', ]
