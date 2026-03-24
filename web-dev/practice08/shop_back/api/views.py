from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product             

def home(request):
    return JsonResponse("This is the API homepage.", safe = False)

def getProducts(request):
    products = Product.objects.values()
    
    return JsonResponse(list(products), safe = False)

def getProduct(request, _id):
    try:
        product = Product.objects.get(id = _id)
        
        productData = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'count': product.count,
            'isActive': product.isActive,
            'category': product.category.id
        }
        
        return JsonResponse(productData)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status = 404)
    
def getCategories(request):
    categories = Category.objects.values()
        
    return JsonResponse(list(categories), safe = False)

def getCategory(request, _id):
    try:
        category = Category.objects.get(id = _id)
        
        categoryData = {
            'id': category.id,
            'name': category.name
        }
        
        return JsonResponse(categoryData)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found.'}, status = 404)
    
def getCategoryProducts(request, _id):
    try:
        category = Category.objects.get(id = _id)
        products = Product.objects.filter(category = category).values()
            
        return JsonResponse(list(products), safe = False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found.'}, status = 404)
    
