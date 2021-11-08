from django.urls import path
from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('usaid/', views.usaid, name='usaid'),
    path('uaid/', views.uaid, name='uaid'),
    path('usavisa/', views.usavisa, name='usavisa'),
]