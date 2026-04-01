from django.urls import path

from . import views as apiViews

urlpatterns = [
    # FBV
    # path("products/", apiViews.productList, name = "product-list"),
    # path("products/<int:productId>/", apiViews.productDetails, name = "product-details"),
    
    # CBV, Mixins
    # path("products/", apiViews.ProductListAPIView.as_view(), name = "product-list"),
    # path("products/<int:productId>/", apiViews.ProductDetailsAPIView.as_view(), name = "product-details"),
    
    # Generics
    path("products/", apiViews.ProductListAPIView.as_view(), name = "product-list"),
    path("products/<int:productId>/", apiViews.ProductDetailsAPIView.as_view(), name = "product-details"),
    
    path("categories/", apiViews.CategoryListAPIView.as_view(), name = "category-list"),
    path("categories/<int:categoryId>/", apiViews.CategoryDetailsAPIView.as_view(), name = "category-details"),
    path("categories/<int:categoryId>/products/", apiViews.CategoryProductsAPIView.as_view(), name = "category-products")
]



