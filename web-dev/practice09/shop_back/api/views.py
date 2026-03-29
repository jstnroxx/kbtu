from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Category, Product             
from .serializers import CategorySerializer, ProductSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    @action(detail = True, methods = ["get"])
    def products(self, request, pk = None):
        currentCategory = self.get_object()
        
        products = Product.objects.filter(category = currentCategory)
        serializer = ProductSerializer(products, many = True)
        
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer