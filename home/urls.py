from django.urls import path
from . import views

urlpatterns = [
    path('index', views.main, name='index'),
    path('info', views.info, name='info'),
]