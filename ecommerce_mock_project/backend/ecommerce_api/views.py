from datetime import datetime
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.utils import timezone
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategorySerializer

class PopularProductsView(APIView):
    def get(self, request):
        current_year = timezone.now().year

        popular_products = Product.objects.filter(order__order_date__year=current_year) \
        .annotate(
            order_count=Count('order'),  
            total_profit=Sum('order__profit')  
        ) \
        .select_related('subcat__category')  \
        .order_by('-order_count')[:3]  

        serializer = ExtendedProductSerializer(popular_products, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CustomersCountView(APIView):
    def get(self, request):
        customers_count = Customer.objects.all().count()
        return Response({'customers_count' : customers_count}, status=status.HTTP_200_OK)
class OrdersCountView(APIView):
    def get(self, request):
        orders_count = Order.objects.all().count()
        return Response({'orders_count' : orders_count}, status=status.HTTP_200_OK)
    
class SalesYearlyOverviewView(APIView):
    def get(self, request):
        current_year = timezone.now().year

        monthly_sales = Order.objects.filter(order_date__year=current_year) \
            .annotate(month=TruncMonth('order_date')) \
            .values('month') \
            .annotate(total_sales=Sum('sales')) \
            .annotate(total_profits=Sum('profit')) \
            .order_by('month')
        
        data = list(monthly_sales)
        return Response(data, status=status.HTTP_200_OK)
    
class SubcategoriesOverviewView(APIView):
    def get(self, request, limit=None):
        current_year = timezone.now().year
        if limit is None:
            limit = int(request.query_params.get('limit', 8))
        else:
            limit = int(limit)

        if limit <= 0 or limit > 24:
            limit = 8

        popular_categories_this_year = Order.objects.filter(order_date__year=current_year) \
            .values('product__subcat__name') \
            .annotate(total_orders=Count('id')) \
            .order_by('-total_orders')[:limit]

        data = list(popular_categories_this_year)
        return Response(data, status=status.HTTP_200_OK)