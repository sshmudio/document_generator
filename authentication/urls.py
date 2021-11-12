from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
