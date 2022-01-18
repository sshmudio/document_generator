from django import forms
from .models import DocUkraineInternational, StateCardUsa, UsaVisa
from confighelper.models import DocumentsFields


class GermanyDocForm(forms.ModelForm):
    class Meta:
        model = DocumentsFields
        fields = [
            'document_type',
            'country_code',
            'surname',
            'given_names',
            'document_number',
            'nationality',
            'birth_date',
            'sex',
            'expiry_date',
            'issue_date',
            'optional_data',
            'photo_document',
            'remove_bg',
            'get_exif_info',
            'background_image',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['document_type'].initial = 'P'
        self.fields['country_code'].initial = 'DEU'
        self.fields['surname'].initial = 'DEUTSCH'
        self.fields['given_names'].initial = 'DEUTSCH'
        self.fields['document_number'].initial = 'CG313WPXP'
        self.fields['nationality'].initial = 'DEUTSCH'
        self.fields['birth_date'].initial = '901212'
        self.fields['sex'].initial = 'M'
        self.fields['expiry_date'].initial = '291212'
        self.fields['issue_date'].initial = '191212'
        self.fields['optional_data'].initial = '12121212'


class DocumentsFieldsForm(forms.ModelForm):
    class Meta:
        model = DocumentsFields
        fields = [
            'document_type',
            'country_code',
            'surname',
            'given_names',
            'document_number',
            'nationality',
            'birth_date',
            'sex',
            'expiry_date',
            'issue_date',
            'optional_data',
            'remove_bg',
            'photo_document',
            'get_exif_info',
            'background_image',
        ]

    # def clean_country_code(self):
    #     country_code = self.cleaned_data.get('country_code')
    #     if len(country_code) > 3:
    #         raise ValidationError('Поле не может быть длинее 3 символов')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['document_type'].initial = 'V'
        self.fields['document_type'].widget.attrs.update({'size': 1, 'class': 'form-control'})
        self.fields['country_code'].initial = 'ITA'
        self.fields['surname'].initial = 'JOHN'
        self.fields['given_names'].initial = 'PETRUCHI'
        self.fields['document_number'].initial = '1212122'
        self.fields['nationality'].initial = 'ITA'
        self.fields['birth_date'].initial = '901212'
        self.fields['sex'].initial = 'F'
        self.fields['expiry_date'].initial = '291212'
        self.fields['issue_date'].initial = '191212'
        self.fields['optional_data'].initial = '12121212'
        self.fields['photo_document'].widget.attrs.update({'size': 1, 'class': 'form-control form-control-sm'})
        self.fields['get_exif_info'].widget.attrs.update({'size': 1, 'class': 'form-control form-control-sm'})
        self.fields['background_image'].widget.attrs.update({'size': 1, 'class': 'form-control form-control-sm'})


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
