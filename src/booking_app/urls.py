from django.urls import path

from . import views
from .views import rules, establishments

urlpatterns = [
    path('rules/', views.rules, name='rules'),
    path('establishments/', views.establishments, name='establishments'),
]
