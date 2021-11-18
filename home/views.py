from pathlib import Path

from django.contrib.auth.decorators import login_required
from django.http.response import FileResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from request_da.ua_int import get_data_from_form
from request_da.us_state import request_info_state_usa_card
from request_da.usa_visa import get_data_from_usa_visa
from wallets.models import UserBalance
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import DocForm, StateCardUsaForm, UsaVisaForm
from .utils import ObjectsHomeMixin


class HomePage(ObjectsHomeMixin, View):
    model = UserBalance
    template = 'home/index.html'
    # context_object_name = 'objects'


class BillingPage(LoginRequiredMixin, ObjectsHomeMixin, View):
    model = UserBalance
    template = 'home/billing.html'


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
                bal.user_balance -= 1
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
            form.save()
            done_image = get_data_from_usa_visa(form.cleaned_data)
            needs_file = Path(done_image).absolute()
            response = FileResponse(open(done_image, 'rb'))
            if bal.user_balance < 1:
                return redirect('/home/billing/')
            else:
                bal.user_balance -= 1
                bal.save()

                return response
    else:
        form = UsaVisaForm()

    return render(request, 'home/usaid.html', {'form': form})
