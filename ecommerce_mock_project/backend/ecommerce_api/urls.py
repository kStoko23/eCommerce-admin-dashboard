from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from ecommerce_api.views import CategoryViewSet, CityViewSet, CustomerViewSet, OrderViewSet, ProductViewSet, StateViewSet, SubCategoryViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'cities', CityViewSet)
router.register(r'states', StateViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]