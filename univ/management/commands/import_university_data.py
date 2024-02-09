# your_django_app/management/commands/import_university_data.py
from django.core.management.base import BaseCommand
from univ.utils.import_data import import_data_from_csv

class Command(BaseCommand):
    help = 'Imports data from a CSV file into the University model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        import_data_from_csv(file_path)
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
