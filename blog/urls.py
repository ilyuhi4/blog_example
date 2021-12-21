from django.urls import path
from .views import first_index

urlpatterns = [
    path('', first_index, name='first_index'),
]