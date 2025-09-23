from django.urls import path
from .views import *

urlpatterns = [
    path('matematicas/', matematicas, name='matematicas'),
    path('historia/', historia, name='historia'),  # Nueva ruta para la vista historia
    path('ciencias/', ciencias, name='ciencias'),  # Nueva ruta para la
]