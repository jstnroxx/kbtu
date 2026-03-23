from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product             

def productList(request):
    products = Product.objects.all()
    productData = []
    
    for product in products:
        productData.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'count': product.count,
            'isActive': product.isActive,
            'category': product.category.id
        })
    
    return JsonResponse(productData, safe = False)

def productDetails(request, id):
    try:
        product = Product.objects.get(id = id)
        
        productData = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'count': product.count,
            'isActive': product.isActive,
            'category': product.category.id
        }
        
        return JsonResponse(productData, safe = False)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status = 404)
    
def categoryList(request):
    categories = Category.objects.all()
    categoryData = []
    
    for category in categories:
        categoryData.append({
            'id': category.id,
            'name': category.name
        })
        
    return JsonResponse(categoryData, safe = False)

def categoryDetails(request, id):
    try:
        category = Category.objects.get(id = id)
        
        categoryData = {
            'id': category.id,
            'name': category.name
        }
        
        return JsonResponse(categoryData)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found.'}, status = 404)
    
def categoryProducts(request, id):
    try:
        category = Category.objects.get(id = id)
        products = Product.objects.filter(category = category)
        productData = []
        
        for product in products:
            productData.append({
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'count': product.count,
                'isActive': product.isActive,
                'category': product.category.id
            })
            
        return JsonResponse(productData, safe = False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found.'}, status = 404)