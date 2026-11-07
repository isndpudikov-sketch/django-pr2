from django.urls import path
from . import views

app_name = 'agency'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('about/contacts/', views.contacts_view, name='contacts'),
    path('about/location/', views.location_view, name='location'),
    path('tours/', views.tours_view, name='tours'),
    path('services/', views.services_view, name='services'),
]