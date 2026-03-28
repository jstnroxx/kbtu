from django.core.management.base import BaseCommand
from api.models import Category, Product

class Command(BaseCommand):
    help = "Clears database 'Categories' and 'Products' tables."
    
    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS("Deleted database data successfully."))