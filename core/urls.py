from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('idgenerator/', include('idgenerator.urls'))

]
