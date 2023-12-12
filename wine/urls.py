from django.urls import path
from .views import wine

urlpatterns = [
    path('', wine, name='wine'),
]