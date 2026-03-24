from django.urls import path
from . import views as apiViews

urlpatterns = [
    path('', apiViews.home, name = "api-home"),
    path('products/', apiViews.getProducts, name = "product-list"),
    path('products/<int:_id>/', apiViews.getProduct, name = "product-details"),
    path('categories/', apiViews.getCategories, name = "category-list"),
    path('categories/<int:_id>/', apiViews.getCategory, name = "category-details"),
    path('categories/<int:_id>/products/', apiViews.getCategoryProducts, name = "category-products"),
]