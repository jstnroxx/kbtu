from django.core.management.base import BaseCommand
from django.db import connection
from api.models import Category, Product

class Command(BaseCommand):
    help = "Clears database 'Categories' and 'Products' tables and resets ID counters."
    
    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()
        
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'api_category';")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'api_product';")
        
        self.stdout.write("[SUCCESS]: Deleted database data and reset ID's successfully.")