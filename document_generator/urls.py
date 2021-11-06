from django.urls import include, path  
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', include('idgenerator.urls')),
    path('admin/', admin.site.urls),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

