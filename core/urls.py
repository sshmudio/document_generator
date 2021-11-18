from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('authentication.urls')),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
