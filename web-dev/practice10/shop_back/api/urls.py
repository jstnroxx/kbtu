from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views as apiViews

router = DefaultRouter()

router.register(r"categories", apiViews.CategoryViewSet, basename = "category")
router.register(r"products", apiViews.ProductViewSet, basename = "product")

urlpatterns = [
    path('', include(router.urls)),
]