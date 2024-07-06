from datetime import datetime, timedelta
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.utils import timezone
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
from django.utils.dateparse import parse_date
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
        """
        Handle GET request to retrieve the count of customers who placed orders.

        Query Parameters:
            time_period (str, optional): Filter orders by a predefined time period ('last_year', 'last_month', 'last_week').
            start_date (str, optional): Filter orders from this start date (format: 'YYYY-MM-DD').
            end_date (str, optional): Filter orders up to this end date (format: 'YYYY-MM-DD').

        Returns:
            Response: A JSON response containing the count of customers.
        """
        # Get optional URL parameters
        time_period = request.query_params.get('time_period', None)
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)

        # Define the base query to get order data
        orders_query = Order.objects.all()

        # Apply predefined time periods
        if time_period and not (start_date or end_date):
            if time_period == 'last_year':
                one_year_ago = timezone.now() - timedelta(days=365)
                orders_query = orders_query.filter(order_date__gte=one_year_ago)
            elif time_period == 'last_month':
                one_month_ago = timezone.now() - timedelta(days=30)
                orders_query = orders_query.filter(order_date__gte=one_month_ago)
            elif time_period == 'last_week':
                one_week_ago = timezone.now() - timedelta(days=7)
                orders_query = orders_query.filter(order_date__gte=one_week_ago)

        # Apply specific date range filters
        if start_date:
            start_date_parsed = parse_date(start_date)
            if start_date_parsed:
                orders_query = orders_query.filter(order_date__gte=start_date_parsed)
        if end_date:
            end_date_parsed = parse_date(end_date)
            if end_date_parsed:
                orders_query = orders_query.filter(order_date__lte=end_date_parsed)

        # Count unique customers based on their orders
        customers_count = orders_query.values('customer_id').distinct().count()

        return Response({'customers_count': customers_count}, status=status.HTTP_200_OK)
class OrdersCountView(APIView):
    def get(self, request):
        """
        Handle GET request to retrieve the count of orders.

        Query Parameters:
            time_period (str, optional): Filter orders by a predefined time period ('last_year', 'last_month', 'last_week').
            start_date (str, optional): Filter orders from this start date (format: 'YYYY-MM-DD').
            end_date (str, optional): Filter orders up to this end date (format: 'YYYY-MM-DD').

        Returns:
            Response: A JSON response containing the count of orders.
        """
        # Get optional URL parameters
        time_period = request.query_params.get('time_period', None)
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)

        # Get all orders
        orders_query = Order.objects.all()

        # Filter if time_period is provided and start_date and end_date are not provided
        if time_period is not None and (start_date is None and end_date is None):
            if time_period == 'last_year':
                one_year_ago = timezone.now() - timedelta(days=365)
                orders_query = orders_query.filter(order_date__gte=one_year_ago)
            elif time_period == 'last_month':
                one_month_ago = timezone.now() - timedelta(days=30)
                orders_query = orders_query.filter(order_date__gte=one_month_ago)
            elif time_period == 'last_week':
                one_week_ago = timezone.now() - timedelta(days=7)
                orders_query = orders_query.filter(order_date__gte=one_week_ago)

        # Filter if time_period is not provided and either start_date or end_date is provided
        if time_period is None and (start_date or end_date):
            # Filter by start_date if provided
            if start_date:
                start_date_parsed = parse_date(start_date)
                if start_date_parsed:
                    orders_query = orders_query.filter(order_date__gte=start_date_parsed)

            # Filter by end_date if provided
            if end_date:
                end_date_parsed = parse_date(end_date)
                if end_date_parsed:
                    orders_query = orders_query.filter(order_date__lte=end_date_parsed)

        # Count filtered orders
        orders_count = orders_query.count()

        return Response({'orders_count': orders_count}, status=status.HTTP_200_OK)
    
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