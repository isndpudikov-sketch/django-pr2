from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tour, Service, Hotel, Excursion, OfficeEmployee
from .forms import TourForm, ServiceForm, HotelForm, ExcursionForm, OfficeEmployeeForm



def home_view(request):
    return render(request, 'agency/home.html')


def about_view(request):
    return render(request, 'agency/about.html')


def contacts_view(request):
    return render(request, 'agency/contacts.html')


def location_view(request):
    return render(request, 'agency/location.html')



class TourListView(ListView):
    model = Tour
    template_name = 'agency/tours/tour_list.html'
    context_object_name = 'tours'


class TourDetailView(DetailView):
    model = Tour
    template_name = 'agency/tours/tour_detail.html'
    context_object_name = 'tour'


class TourCreateView(CreateView):
    model = Tour
    form_class = TourForm
    template_name = 'agency/tours/tour_form.html'
    success_url = reverse_lazy('agency:tour_list')


class TourUpdateView(UpdateView):
    model = Tour
    form_class = TourForm
    template_name = 'agency/tours/tour_form.html'
    success_url = reverse_lazy('agency:tour_list')


class TourDeleteView(DeleteView):
    model = Tour
    template_name = 'agency/tours/tour_confirm_delete.html'
    context_object_name = 'tour'
    success_url = reverse_lazy('agency:tour_list')



class ServiceListView(ListView):
    model = Service
    template_name = 'agency/services/service_list.html'
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'agency/services/service_detail.html'
    context_object_name = 'service'


class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'agency/services/service_form.html'
    success_url = reverse_lazy('agency:service_list')


class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'agency/services/service_form.html'
    success_url = reverse_lazy('agency:service_list')


class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'agency/services/service_confirm_delete.html'
    context_object_name = 'service'
    success_url = reverse_lazy('agency:service_list')



class HotelListView(ListView):
    model = Hotel
    template_name = 'agency/hotels/hotel_list.html'
    context_object_name = 'hotels'


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'agency/hotels/hotel_detail.html'
    context_object_name = 'hotel'


class HotelCreateView(CreateView):
    model = Hotel
    form_class = HotelForm
    template_name = 'agency/hotels/hotel_form.html'
    success_url = reverse_lazy('agency:hotel_list')


class HotelUpdateView(UpdateView):
    model = Hotel
    form_class = HotelForm
    template_name = 'agency/hotels/hotel_form.html'
    success_url = reverse_lazy('agency:hotel_list')


class HotelDeleteView(DeleteView):
    model = Hotel
    template_name = 'agency/hotels/hotel_confirm_delete.html'
    context_object_name = 'hotel'
    success_url = reverse_lazy('agency:hotel_list')



class ExcursionListView(ListView):
    model = Excursion
    template_name = 'agency/excursions/excursion_list.html'
    context_object_name = 'excursions'


class ExcursionDetailView(DetailView):
    model = Excursion
    template_name = 'agency/excursions/excursion_detail.html'
    context_object_name = 'excursion'


class ExcursionCreateView(CreateView):
    model = Excursion
    form_class = ExcursionForm
    template_name = 'agency/excursions/excursion_form.html'
    success_url = reverse_lazy('agency:excursion_list')


class ExcursionUpdateView(UpdateView):
    model = Excursion
    form_class = ExcursionForm
    template_name = 'agency/excursions/excursion_form.html'
    success_url = reverse_lazy('agency:excursion_list')


class ExcursionDeleteView(DeleteView):
    model = Excursion
    template_name = 'agency/excursions/excursion_confirm_delete.html'
    context_object_name = 'excursion'
    success_url = reverse_lazy('agency:excursion_list')



class EmployeeListView(ListView):
    model = OfficeEmployee
    template_name = 'agency/employees/employee_list.html'
    context_object_name = 'employees'


class EmployeeDetailView(DetailView):
    model = OfficeEmployee
    template_name = 'agency/employees/employee_detail.html'
    context_object_name = 'employee'


class EmployeeCreateView(CreateView):
    model = OfficeEmployee
    form_class = OfficeEmployeeForm
    template_name = 'agency/employees/employee_form.html'
    success_url = reverse_lazy('agency:employee_list')


class EmployeeUpdateView(UpdateView):
    model = OfficeEmployee
    form_class = OfficeEmployeeForm
    template_name = 'agency/employees/employee_form.html'
    success_url = reverse_lazy('agency:employee_list')


class EmployeeDeleteView(DeleteView):
    model = OfficeEmployee
    template_name = 'agency/employees/employee_confirm_delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('agency:employee_list')