from django.urls import path
from . import views

urlpatterns = [
    path('', views.Northern_records, name='Northern_records')
]