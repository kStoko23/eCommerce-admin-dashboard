from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Count
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
        popular_products = Product.objects.annotate(order_count=Count('order')).order_by('-order_count')[:5]
        
        serializer = ProductSerializer(popular_products, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)