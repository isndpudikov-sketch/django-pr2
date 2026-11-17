from django.urls import path
from . import views

app_name = 'agency'

urlpatterns = [
    
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('about/contacts/', views.contacts_view, name='contacts'),
    path('about/location/', views.location_view, name='location'),

    
    path('tours/', views.TourListView.as_view(), name='tour_list'),
    path('tours/<int:pk>/', views.TourDetailView.as_view(), name='tour_detail'),
    path('tours/create/', views.TourCreateView.as_view(), name='tour_create'),
    path('tours/<int:pk>/update/', views.TourUpdateView.as_view(), name='tour_update'),
    path('tours/<int:pk>/delete/', views.TourDeleteView.as_view(), name='tour_delete'),

    
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('services/create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('services/<int:pk>/update/', views.ServiceUpdateView.as_view(), name='service_update'),
    path('services/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),

    
    path('hotels/', views.HotelListView.as_view(), name='hotel_list'),
    path('hotels/<int:pk>/', views.HotelDetailView.as_view(), name='hotel_detail'),
    path('hotels/create/', views.HotelCreateView.as_view(), name='hotel_create'),
    path('hotels/<int:pk>/update/', views.HotelUpdateView.as_view(), name='hotel_update'),
    path('hotels/<int:pk>/delete/', views.HotelDeleteView.as_view(), name='hotel_delete'),

   
    path('excursions/', views.ExcursionListView.as_view(), name='excursion_list'),
    path('excursions/<int:pk>/', views.ExcursionDetailView.as_view(), name='excursion_detail'),
    path('excursions/create/', views.ExcursionCreateView.as_view(), name='excursion_create'),
    path('excursions/<int:pk>/update/', views.ExcursionUpdateView.as_view(), name='excursion_update'),
    path('excursions/<int:pk>/delete/', views.ExcursionDeleteView.as_view(), name='excursion_delete'),

   
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
]