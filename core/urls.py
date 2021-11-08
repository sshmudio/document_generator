from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("authentication.urls")),
    path("home/", include("home.urls")),
    path("idgenerator/", include("idgenerator.urls"))

]
