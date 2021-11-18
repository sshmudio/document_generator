from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('usaid/', usaid, name='usaid'),
    path('uaid/', uaid, name='uaid'),
    path('usavisa/', usavisa, name='usavisa'),
    path('billing/', BillingPage.as_view(), name='billing'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
