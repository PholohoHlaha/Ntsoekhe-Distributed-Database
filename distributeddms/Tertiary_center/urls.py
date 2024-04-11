from django.urls import path
from . import views

urlpatterns = [
    path('Tertiary_center', views.Tertiary_centerView, name='Tertiary_center')
]