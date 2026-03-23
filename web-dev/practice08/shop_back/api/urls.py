from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.productList, name = "ProductList"),
    path('products/<int:id>/', views.productDetails, name = "ProductDetails"),
    path('categories/', views.categoryList, name = "CategoryList"),
    path('categories/<int:id>/', views.categoryDetails, name = "CategoryDetails"),
    path('categories/<int:id>/products/', views.categoryProducts, name = "CategoryProducts"),
]