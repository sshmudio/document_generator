# -*- encoding: utf-8 -*-
from pathlib import Path
from django.contrib.auth.decorators import login_required
from django.http.response import FileResponse
from django.shortcuts import render
from authentication.models import UserBalance
from home.forms import DocForm, StateCardUsaForm, UsaVisaForm
from request_da.ua_int import get_data_from_form
from request_da.us_state import request_info_state_usa_card
from request_da.usa_visa import get_data_from_usa_visa
from decimal import *
from django.views.generic import View
from .utils import ObjectsHomeMixin


class HomePage(ObjectsHomeMixin, View):
    model = UserBalance
    template = 'home/index.html'


class BillingPage(ObjectsHomeMixin, View):
    model = UserBalance
    template = 'home/billing.html'


@login_required(login_url="/login/")
def uaid(request):
    if request.method == 'POST':
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            done_image = get_data_from_form(form.cleaned_data)
            images_result = Path(done_image).absolute()
            response = FileResponse(open(done_image, 'rb'))
            return response
    else:
        form = DocForm()

    return render(request, 'home/uaid.html', {'form': form})


@login_required(login_url="/login/")
def usaid(request):
    bal = UserBalance.objects.get(user_id=request.user.id)
    print(bal.balance)
    if request.method == 'POST':
        form = StateCardUsaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            done_image = request_info_state_usa_card(form.cleaned_data)
            needs_file = Path(done_image).absolute()
            response = FileResponse(open(done_image, 'rb'))
            bal.balance -= 1
            bal.save()
            return response

    else:
        form = StateCardUsaForm()

    return render(request, 'home/usaid.html', {'form': form})


@login_required(login_url="/login/")
def usavisa(request):
    if request.method == 'POST':
        form = UsaVisaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            done_image = get_data_from_usa_visa(form.cleaned_data)
            needs_file = Path(done_image).absolute()
            response = FileResponse(open(done_image, 'rb'))
            return response
    else:
        form = UsaVisaForm()

    return render(request, 'home/usaid.html', {'form': form})
