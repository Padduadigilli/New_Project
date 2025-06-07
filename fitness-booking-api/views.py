from rest_framework import generics, status
from rest_framework.response import Response
from django.utils import timezone
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingCreateSerializer, BookingSerializer

class FitnessClassListView(generics.ListAPIView):
    queryset = FitnessClass.objects.filter(datetime__gt=timezone.now())
    serializer_class = FitnessClassSerializer

class CreateBookingView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        fitness_class = serializer.validated_data['fitness_class']
        
        if fitness_class.available_slots <= 0:
            return Response(
                {"detail": "No available slots for this class"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create booking
        booking = Booking.objects.create(**serializer.validated_data)
        
        # Update available slots
        fitness_class.available_slots -= 1
        fitness_class.save()
        
        return Response(
            BookingSerializer(booking).data,
            status=status.HTTP_201_CREATED
        )

class UserBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    
    def get_queryset(self):
        email = self.request.query_params.get('email')
        return Booking.objects.filter(client_email=email)