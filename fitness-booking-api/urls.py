from django.urls import path
from .views import FitnessClassListView, CreateBookingView, UserBookingsView

urlpatterns = [
    path('classes/', FitnessClassListView.as_view(), name='class-list'),
    path('book/', CreateBookingView.as_view(), name='create-booking'),
    path('bookings/', UserBookingsView.as_view(), name='user-bookings'),
]

