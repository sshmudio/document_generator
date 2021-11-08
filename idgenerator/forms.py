from django import forms 
from .models import DocUkraineInternational, StateCardUsa
from django import forms


class DocForm(forms.ModelForm):
    class Meta:
        model = DocUkraineInternational
        fields = [
            'given_name',
            'surname',
            'passport_number',
            'genre',
            'birth_date',
            'locations',
            'photo_doc',
            'remove_bg',
            'get_exif_info',
            'background_image']


class StateCardUsaForm(forms.ModelForm):
    class Meta:
        model = StateCardUsa
        fields = [
            'passport_card_number',
            'nationality',
            'surname',
            'given_names',
            'sex',
            'date_of_birdth',
            'place_of_birth',
            'issues_on',
            'expiries_on',
            'documment_id',
            'photo_document',
            'remove_bg',
            'get_exif_info',
            'background_image',]



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)