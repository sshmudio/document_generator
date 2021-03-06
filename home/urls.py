from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.http.response import HttpResponseRedirect

from .views import *

urlpatterns = [

    path('', HomePage.as_view(), name='index'),
    path('usaid/', usaid, name='usaid'),
    path('uaid/', uaid, name='uaid'),
    path('usavisa/', usavisa, name='usavisa'),
    path('billing/', BillingPage.as_view(), name='billing'),
    path('italy/', GeneratorFormView.as_view(), name='italy'),
    path('germany/', GermanyFormView.as_view(), name='germany'),
    path('profile/', UserProfile.as_view(), name='profile'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


def entry_not_found(request, exception):
    return HttpResponseRedirect('/')
