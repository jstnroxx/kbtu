from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Category, Product
from api.serializers import CategorySerializer, ProductSerializer

class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    lookup_url_kwarg = "productId"

class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    lookup_url_kwarg = "categoryId"

class CategoryProductsAPIView(APIView):
    def get(self, request, categoryId):
        try:
            category = Category.objects.get(pk = categoryId)
        except Category.DoesNotExist:
            return Response({"error" : "category not found"}, status = status.HTTP_404_NOT_FOUND)
        
        products = Product.objects.filter(category = category)
        serializer = ProductSerializer(products, many = True)
        
        return Response(serializer.data)