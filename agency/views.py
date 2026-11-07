from django.shortcuts import render

def home_view(request):
    return render(request, 'agency/home.html')

def about_view(request):
    return render(request, 'agency/about.html')

def contacts_view(request):
    return render(request, 'agency/contacts.html')

def location_view(request):
    return render(request, 'agency/location.html')

def tours_view(request):
    return render(request, 'agency/tours.html')

def services_view(request):
    return render(request, 'agency/services.html')