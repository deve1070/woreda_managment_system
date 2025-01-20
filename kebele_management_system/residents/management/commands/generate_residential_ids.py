from django.core.management.base import BaseCommand
from residents.models import ResidentialID
import random
import string

class Command(BaseCommand):
    help = "Generate Residential IDs"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Number of Residential IDs to generate")

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for _ in range(count):
            id_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            ResidentialID.objects.create(id_number=id_number)
        self.stdout.write(self.style.SUCCESS(f'Successfully generated {count} Residential IDs.'))
