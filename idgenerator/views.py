from pathlib import Path
from django.http import FileResponse
from django.shortcuts import render
from request_da.request_data import get_data_from_form
from request_da.request_state_usa_card import request_info_state_usa_card

from idgenerator.forms import DocForm, StateCardUsaForm


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
    return render(request, 'home/uaid.html', context={'form': form})


def usaid(request):
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

    return render(request, 'home/usaid.html', context={'form': form})
