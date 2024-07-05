from rest_framework import serializers
from django.utils import timezone
from django.db.models import Sum
from .models import Category, City, Customer, Product, Order, Region, State, Subcategory

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ExtendedProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='subcat.category.name')
    product_id = serializers.IntegerField(source='id')
    product_name = serializers.CharField(source='name')
    order_count = serializers.SerializerMethodField()
    total_profit = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('product_id', 'product_name', 'category_name', 'order_count', 'total_profit')

    def get_order_count(self, obj):
        return obj.order_set.filter(order_date__year=timezone.now().year).count()

    def get_total_profit(self, obj):
        return obj.order_set.filter(order_date__year=timezone.now().year).aggregate(Sum('profit'))['profit__sum'] or 0


class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name')
    product_name = serializers.CharField(source='product.name')
    city_name = serializers.CharField(source='city.name')
    state_name = serializers.CharField(source='state.name')

    class Meta:
        model = Order
        fields = '__all__'
        depth = 1  # Alternatywnie, można ustawić głębokość, aby automatycznie zagnieżdżać powiązane obiekty


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'
