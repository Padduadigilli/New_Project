from django.core.management.base import BaseCommand
from bookings.models import FitnessClass
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seed the database with sample fitness classes'

    def handle(self, *args, **options):
        # Clear existing data
        FitnessClass.objects.all().delete()

        # Create sample classes
        classes = [
            FitnessClass(
                name="Yoga",
                datetime=timezone.now() + timedelta(days=1),
                instructor="John Doe",
                max_slots=15,
                available_slots=15
            ),
            FitnessClass(
                name="Zumba",
                datetime=timezone.now() + timedelta(days=2),
                instructor="Jane Smith",
                max_slots=20,
                available_slots=20
            ),
            FitnessClass(
                name="HIIT",
                datetime=timezone.now() + timedelta(hours=5),
                instructor="Mike Johnson",
                max_slots=10,
                available_slots=10
            )
        ]

        FitnessClass.objects.bulk_create(classes)
        self.stdout.write(self.style.SUCCESS('Successfully seeded fitness classes'))