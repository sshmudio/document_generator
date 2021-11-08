# -*- encoding: utf-8 -*-
from pathlib import Path
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import FileResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from idgenerator.forms import DocForm, StateCardUsaForm
from request_da.request_data import get_data_from_form
from request_da.request_state_usa_card import request_info_state_usa_card


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    return render(request, 'home/index.html', context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


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

    return render(request, 'home/usaid.html', {'form': form})
