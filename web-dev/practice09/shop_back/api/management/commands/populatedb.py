from django.core.management import call_command
from django.core.management.base import BaseCommand
from api.models import Category, Product


class Command(BaseCommand):
    help = "Insert sample data into the database 'Category' and 'Product' tables. CLEARS DATA!"
    
    def handle(self, *args, **kwargs):
        call_command("cleardb")
        
        # Categories
        electronics = Category.objects.create(name = "Electronics")
        clothing = Category.objects.create(name = "Clothing")
        books = Category.objects.create(name = "Books")
        sports = Category.objects.create(name = "Sports")
        home = Category.objects.create(name = "Home & Kitchen")
        
        productsData = [
            
            # Electronics
            {
                "name": "Laptop",
                "price": 999.99,
                "description": "High-performance laptop with 16GB RAM",
                "count": 15,
                "isActive": True,
                "category": electronics
            },
            {
                "name": "Smartphone",
                "price": 699.99,
                "description": "Latest model smartphone with 128GB storage",
                "count": 25,
                "isActive": True,
                "category": electronics
            },
            {
                "name": "Wireless Headphones",
                "price": 149.99,
                "description": "Noise-cancelling Bluetooth headphones",
                "count": 40,
                "isActive": True,
                "category": electronics
            },
            {
                "name": "Tablet",
                "price": 399.99,
                "description": "10-inch tablet perfect for reading and browsing",
                "count": 0,
                "isActive": False,
                "category": electronics
            },
            
            # Clothing
            {
                "name": "T-Shirt",
                "price": 19.99,
                "description": "Cotton t-shirt, available in multiple colors",
                "count": 100,
                "isActive": True,
                "category": clothing
            },
            {
                "name": "Jeans",
                "price": 49.99,
                "description": "Classic blue denim jeans",
                "count": 60,
                "isActive": True,
                "category": clothing
            },
            {
                "name": "Winter Jacket",
                "price": 89.99,
                "description": "Warm winter jacket with hood",
                "count": 30,
                "isActive": True,
                "category": clothing
            },
            {
                "name": "Summer Dress",
                "price": 39.99,
                "description": "Light and comfortable summer dress",
                "count": 5,
                "isActive": True,
                "category": clothing
            },
            
            # Books
            {
                "name": "Python Programming Guide",
                "price": 29.99,
                "description": "Complete guide to Python programming for beginners",
                "count": 50,
                "isActive": True,
                "category": books
            },
            {
                "name": "Web Development Basics",
                "price": 34.99,
                "description": "Learn HTML, CSS, and JavaScript",
                "count": 35,
                "isActive": True,
                "category": books
            },
            {
                "name": "Science Fiction Novel",
                "price": 14.99,
                "description": "Bestselling sci-fi adventure",
                "count": 80,
                "isActive": True,
                "category": books
            },
            
            # Sports
            {
                "name": "Basketball",
                "price": 24.99,
                "description": "Official size basketball",
                "count": 45,
                "isActive": True,
                "category": sports
            },
            {
                "name": "Yoga Mat",
                "price": 19.99,
                "description": "Non-slip yoga mat with carrying strap",
                "count": 70,
                "isActive": True,
                "category": sports
            },
            {
                "name": "Running Shoes",
                "price": 79.99,
                "description": "Lightweight running shoes with cushioned sole",
                "count": 0,
                "isActive": False,
                "category": sports
            },
            
            # Home & Kitchen
            {
                "name": "Coffee Maker",
                "price": 59.99,
                "description": "Programmable coffee maker with timer",
                "count": 20,
                "isActive": True,
                "category": home
            },
            {
                "name": "Blender",
                "price": 39.99,
                "description": "High-speed blender for smoothies",
                "count": 15,
                "isActive": True,
                "category": home
            },
            {
                "name": "Cookware Set",
                "price": 129.99,
                "description": "10-piece non-stick cookware set",
                "count": 12,
                "isActive": True,
                "category": home
            },
            {
                "name": "Vacuum Cleaner",
                "price": 199.99,
                "description": "Powerful vacuum cleaner with HEPA filter",
                "count": 8,
                "isActive": True,
                "category": home
            },
        ]
        
        for productData in productsData:
            Product.objects.create(**productData)
            
        self.stdout.write("[SUCCESS]: Cleared tables and inserted sample data successfully.")