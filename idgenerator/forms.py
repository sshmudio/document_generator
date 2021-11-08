from django import forms
from .models import DocUkraineInternational, StateCardUsa, UsaVisa


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
            'background_image', ]

class UsaVisaForm(forms.ModelForm):
    class Meta:
        model = UsaVisa
        fields = [
            'doc_type',
            'doc_country',
            'surname',
            'givenname',
            'doc_number',
            'nationality',
            'birthdate',
            'genre',
            'doc_exp_date',
            'optional_data',
            'photo_document',
            'remove_bg',
            'get_exif_info',
            'background_image',
        ]