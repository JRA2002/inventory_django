from django.urls import path
from .views import HomeView

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    
]