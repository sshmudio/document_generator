from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from request_da.request_state_usa_card import request_info_state_usa_card
from .forms import DocForm, StateCardUsaForm
from request_da.request_data import get_data_from_form
from pathlib import Path
from django.http import FileResponse
from django.contrib.auth.decorators import login_required

class HomeViews(View):
    template_name = "idgenerator/home.html"
    @login_required(login_url='/idgenerator/login/')
    def get(self, request):
        return render(request, self.template_name, {})

def ua_doc(request):
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
    return render(request, 'idgenerator/ukid.html', context={'form': form})


def get_name(request):
    if request.method == 'POST':
        form = StateCardUsaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            done_image = request_info_state_usa_card(form.cleaned_data)
            needs_file = Path(done_image).absolute()
            response = FileResponse(open(done_image, 'rb'))
            return response
    else:
        form = StateCardUsaForm()

    return render(request, 'idgenerator/state_card_usa.html', context={'form': form})
