from django.urls import path
from . import views

urlpatterns = [
    path('hospital_center', views.Hospital_centerView, name='hospital_center')
]