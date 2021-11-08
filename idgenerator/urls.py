from django.urls import path
from .views import usaid, uaid
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('usaid/', usaid, name='usaid'),
    path('uaid/', uaid, name='uaid'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
