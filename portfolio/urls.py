from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('enviar_email/', views.enviar_email, name='enviar_email'),
]   
