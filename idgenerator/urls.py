from django.urls import path
from . import views

urlpatterns = [
    path('usaid/', views.usaid, name='usaid'),
    path('uaid/', views.uaid, name='uaid'),
    path('usavisa/', views.usavisa, name='usavisa'),
]
