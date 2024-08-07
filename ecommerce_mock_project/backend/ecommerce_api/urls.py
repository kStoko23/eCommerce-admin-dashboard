from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from ecommerce_api.views import *

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
    path('popular-products/', PopularProductsView.as_view(), name='popular-products'),
    path('count-customers/', CustomersCountView.as_view(), name='count-customers'),
    path('count-orders/', OrdersCountView.as_view(), name='count-orders'),
    path('sales-yearly/', SalesYearlyOverviewView.as_view(), name='sales-yearly'),
    path('categories-yearly/', SubcategoriesOverviewView.as_view(), name='categories-yearly'),
    path('categories-yearly/<int:limit>/', SubcategoriesOverviewView.as_view(), name='categories-yearly-limit'),
]