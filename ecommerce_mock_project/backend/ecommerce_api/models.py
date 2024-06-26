from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=255)
    subcat = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Region(models.Model):
    name = models.CharField(max_length=255)

class State(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class Customer(models.Model):
    name = models.CharField(max_length=255)

class Order(models.Model):
    SHIPMODE_CHOICES = [
        ('Second Class', 'Second Class'),
        ('Standard Class', 'Standard Class'),
        ('First Class', 'First Class'),
        ('Same Day', 'Same Day')
    ]

    SEGMENT_CHOICES = [
        ('Consumer', 'Consumer'),
        ('Corporate', 'Corporate'),
        ('Home Office', 'Home Office')
    ]

    order_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sales = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    ship_date = models.DateField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=50)
    shipmode = models.CharField(max_length=20, choices=SHIPMODE_CHOICES)
    segment = models.CharField(max_length=20, choices=SEGMENT_CHOICES)
