# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('usaid/', views.usaid, name='usaid'),
    path('uaid/', views.uaid, name='uaid'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
