from pathlib import Path
from mrz.generator.mrva import MRVACodeGenerator
from mrz.generator.td3 import *
from django.views.generic.edit import FormView
import re
from django.contrib.auth.decorators import login_required
from django.http.response import FileResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from django.views.generic.list import ListView
from request_da.ua_int import get_data_from_form
from request_da.us_state import request_info_state_usa_card
from request_da.usa_visa import get_data_from_usa_visa
from wallets.models import UserBalance, UserHistory
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DocForm, StateCardUsaForm, UsaVisaForm, DocumentsFieldsForm, GermanyDocForm
from .utils import ObjectsHomeMixin, ObjectsProfileMixin
from confighelper.models import DocumentsFields
from plow.basecreator import Imager


class UserProfile(LoginRequiredMixin, ObjectsProfileMixin,  View):
    model = UserBalance
    template = 'home/profile.html'


class HomePage(ObjectsHomeMixin, View):
    model = UserBalance
    template = 'home/index.html'
    # context_object_name = 'objects'


class BillingPage(LoginRequiredMixin, ObjectsHomeMixin, ListView):
    model = UserHistory
    template = 'home/billing.html'
    context_object_name = 'history'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["history"] = UserHistory.objects.get(user=self.request.user)
        print(context)
        return context


class GeneratorFormView(LoginRequiredMixin, FormView):
    model = DocumentsFields
    form_class = DocumentsFieldsForm
    template_name = 'home/forms.html'
    context_object_name = 'objects'
    success_url = '/home/profile/'

    def get_form_class(self):
        return super().get_form_class()

    def get_form_kwargs(self):
        kwargs = {'initial': self.get_initial()}
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })

        return kwargs

    def form_valid(self, form):
        # self.object = form.save()
        r_info = str(self.request.path.split('/')[-2:-1])
        country = re.sub("[^A-Za-z0-9]", "", r_info)
        document_type = form.cleaned_data['document_type']
        country_code = form.cleaned_data['country_code']
        surname = form.cleaned_data['surname']
        given_names = form.cleaned_data['given_names']
        document_number = form.cleaned_data['document_number']
        nationality = form.cleaned_data['nationality']
        birth_date = form.cleaned_data['birth_date']
        sex = form.cleaned_data['sex']
        expiry_date = form.cleaned_data['expiry_date']
        issue_date = form.cleaned_data.get('issue_date')
        photo_document = form.cleaned_data['photo_document']
        remove_bg = form.cleaned_data['remove_bg']
        get_exif_info = form.cleaned_data['get_exif_info']
        background_image = form.cleaned_data['background_image']

        mrz = MRVACodeGenerator(
            document_type, country_code, surname, given_names, document_number, nationality, birth_date, sex,
            expiry_date, transliteration=dictionary.latin_based(),
            force=False)
        kw = {
            'document_type': form.cleaned_data['document_type'],
            'country_code': form.cleaned_data['country_code'],
            'surname': form.cleaned_data['surname'],
            'given_names': form.cleaned_data['given_names'],
            'document_number': form.cleaned_data['document_number'],
            'nationality': form.cleaned_data['nationality'],
            'birth_date': form.cleaned_data['birth_date'],
            'sex': form.cleaned_data['sex'],
            'expiry_date': form.cleaned_data['expiry_date'],
            'issue_date': form.cleaned_data.get('issue_date'),
            'optional_data': form.cleaned_data['optional_data']
        }
        im = Imager(photo_document, background_image, get_exif_info, True)
        withoutbginfo = im.info_paste(self.request.user, str(mrz), **kw)
        path_done_image = im.paste_background(withoutbginfo)
        bal = UserBalance.objects.get(username_id=self.request.user.id)
        bal.user_balance -= 1
        bal.save()
        h = UserHistory.objects.create(user=self.request.user, cost=3,
                                       document='Italy International', document_path=path_done_image)
        h.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["objects"] = UserBalance.objects.filter(username=self.request.user)
        return context


class GermanyFormView(GeneratorFormView):
    model = DocumentsFields
    form_class = GermanyDocForm

    def form_valid(self, form):
        # self.object = form.save()
        r_info = str(self.request.path.split('/')[-2:-1])
        country = re.sub("[^A-Za-z0-9]", "", r_info)
        document_type = form.cleaned_data['document_type']
        country_code = form.cleaned_data['country_code']
        surname = form.cleaned_data['surname']
        given_names = form.cleaned_data['given_names']
        document_number = form.cleaned_data['document_number']
        nationality = form.cleaned_data['nationality']
        birth_date = form.cleaned_data['birth_date']
        sex = form.cleaned_data['sex']
        expiry_date = form.cleaned_data['expiry_date']
        issue_date = form.cleaned_data.get('issue_date')
        photo_document = form.cleaned_data['photo_document']
        remove_bg = form.cleaned_data['remove_bg']
        get_exif_info = form.cleaned_data['get_exif_info']
        background_image = form.cleaned_data['background_image']

        mrz = TD3CodeGenerator(
            document_type, country_code, surname, given_names, document_number, nationality, birth_date, sex,
            expiry_date, transliteration=dictionary.latin_based(),
            force=False)
        kw = {
            'document_type': form.cleaned_data['document_type'],
            'country_code': form.cleaned_data['country_code'],
            'surname': form.cleaned_data['surname'],
            'given_names': form.cleaned_data['given_names'],
            'document_number': form.cleaned_data['document_number'],
            'nationality': form.cleaned_data['nationality'],
            'birth_date': form.cleaned_data['birth_date'],
            'sex': form.cleaned_data['sex'],
            'expiry_date': form.cleaned_data['expiry_date'],
            'issue_date': form.cleaned_data.get('issue_date'),
            'optional_data': form.cleaned_data['optional_data']
        }
        im = Imager(photo_document, background_image, get_exif_info, True)
        withoutbginfo = im.info_paste(self.request.user, str(mrz), **kw)
        path_done_image = im.paste_background(withoutbginfo)
        bal = UserBalance.objects.get(username_id=self.request.user.id)
        bal.user_balance -= 1
        bal.save()
        h = UserHistory.objects.create(user=self.request.user, cost=3,
                                       document='Italy International', document_path=path_done_image)
        h.save()
        return super().form_valid(form)


@login_required(login_url="/login/")
def uaid(request):
    bal = UserBalance.objects.get(username_id=request.user.id)
    print(bal)
    if request.method == 'POST':
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            done_image = get_data_from_form(form.cleaned_data)
            images_result = Path(done_image).absolute()

            response = FileResponse(open(done_image, 'rb'))
            if bal.user_balance < 1:
                return redirect('/home/billing/')
            else:
                bal.user_balance -= 1
                bal.save()
                return response

    else:
        form = DocForm()
    return render(request, 'home/uaid.html', {'form': form})


@login_required(login_url="/login/")
def usaid(request):
    bal = UserBalance.objects.get(username_id=request.user.id)
    if request.method == 'POST':
        form = StateCardUsaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            done_image = request_info_state_usa_card(form.cleaned_data)
            needs_file = Path(done_image).absolute()
            response = FileResponse(open(done_image, 'rb'))
            if bal.user_balance < 1:
                return redirect('/home/billing/')
            else:
                bal.user_balance -= 3
                bal.save()

                return response

    else:

        form = StateCardUsaForm()
        print('_________\n\n\n\n\n______________')
    # info_user = request.user
    return render(request, 'home/usaid.html', {'form': form})


@login_required(login_url="/login/")
def usavisa(request):
    bal = UserBalance.objects.get(username_id=request.user.id)
    if request.method == 'POST':
        form = UsaVisaForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            done_image = get_data_from_usa_visa(form.cleaned_data)
            needs_file = Path(done_image).absolute()
            response = FileResponse(open(done_image, 'rb'))
            if bal.user_balance < 1:
                return redirect('/home/billing/')
            else:
                bal.user_balance -= 3
                bal.save()

                return response
    else:
        form = UsaVisaForm()

    return render(request, 'home/usaid.html', {'form': form})


def lgut(request):
    return redirect('/home/')
