from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('us/', get_name, name='stateusacard'),
    path('ua_doc/', ua_doc, name='ua_doc'),
] + static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)