from django.contrib import admin
from .models import FitnessClass, Booking

@admin.register(FitnessClass)
class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'datetime', 'instructor', 'available_slots')
    list_filter = ('datetime', 'instructor')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email', 'fitness_class', 'booking_time')
    list_filter = ('booking_time', 'fitness_class')