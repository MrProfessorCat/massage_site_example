from django.urls import path
from . import views

app_name = 'massage_salon'

urlpatterns = [
    path('', views.index, name='index'),
    path('prices/', views.prices, name='prices'),
    path('about/', views.about, name='about'),
]
