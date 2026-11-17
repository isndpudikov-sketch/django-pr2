from django.contrib import admin
from .models import (
    Country, TourCategory, Tour, Service,
    Hotel, Excursion, OfficeEmployee, EmployeeBadge
)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(TourCategory)
class TourCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass


@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    pass


@admin.register(OfficeEmployee)
class OfficeEmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(EmployeeBadge)
class EmployeeBadgeAdmin(admin.ModelAdmin):
    pass