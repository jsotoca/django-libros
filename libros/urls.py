from django.urls import path
from .views import libros_views

urlpatterns = [
    path('libros/',libros_views)
]

