from django.urls import path
from . import views

# app_name = 'daterange_filter'

urlpatterns = [
    path('', views.my_view, name='my_view'),
]
