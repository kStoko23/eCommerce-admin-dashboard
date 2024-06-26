# E-commerce Mock Data Generator

This project generates synthetic data for an e-commerce admin application built using Django and populates a PostgreSQL database with the generated data.

## Usage

Run the data generator script:

```sh
python path/to/script/data_gen.py
```

## Code Overview

### Module imports

```python
import os
import django
import random
from faker import Faker
from django.utils import timezone
from ecommerce_api.models import Category, Subcategory, Product, Customer, Region, State, City, Order
```

Faker is used for generating mock test data. Django models previously used for creating DB are imported from models.py

### Django and faker setup

```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_mock.settings')
django.setup()
fake = Faker()
```

### Data generation methods

```python
def generate_categories():
    categories = ['Computers', 'Phones', 'TV', 'Watches', 'Tablets', 'Home Appliances', 'Audio']
    category_objects = [Category(name=category) for category in categories]
    Category.objects.bulk_create(category_objects)
    return category_objects

def generate_subcategories(categories):
    subcategory_data = {
        'Computers': ['Laptops', 'Desktops', 'Components', 'Peripherals'],
        'Phones': ['Smartphones', 'Landline Phones', 'Phone Accessories'],
        'TV': ['LED TVs', 'OLED TVs', 'Smart TVs', 'TV Accessories'],
        'Watches': ['Smartwatches', 'Analog Watches', 'Digital Watches'],
        'Tablets': ['Android Tablets', 'iPads', 'Windows Tablets'],
        'Home Appliances': ['Refrigerators', 'Washing Machines', 'Microwaves', 'Vacuum Cleaners'],
        'Audio': ['Headphones', 'Speakers', 'Soundbars']
    }
    subcategory_objects = []
    for category in categories:
        for subcat_name in subcategory_data[category.name]:
            subcategory_objects.append(Subcategory(name=subcat_name, category=category))
    Subcategory.objects.bulk_create(subcategory_objects)
    return subcategory_objects

def generate_products(subcategories):
    product_data = {
        'Laptops': ['Dell XPS 13', 'MacBook Pro', 'HP Spectre x360', 'Lenovo ThinkPad'],
        'Desktops': ['iMac', 'HP Pavilion', 'Dell Inspiron', 'Acer Aspire'],
        'Components': ['Intel i9 CPU', 'NVIDIA RTX 3080', 'Samsung 970 EVO SSD', 'Corsair RAM'],
        'Peripherals': ['Logitech Mouse', 'Mechanical Keyboard', '27" Monitor', 'Webcam'],
        'Smartphones': ['iPhone 13', 'Samsung Galaxy S21', 'Google Pixel 6', 'OnePlus 9'],
        'Landline Phones': ['Panasonic Cordless', 'AT&T CL84107', 'VTech CS6719', 'Motorola CD5011'],
        'Phone Accessories': ['Phone Case', 'Screen Protector', 'Wireless Charger', 'Phone Stand'],
        'LED TVs': ['Samsung QLED', 'LG LED', 'Sony Bravia', 'Vizio D-Series'],
        'OLED TVs': ['LG OLED', 'Sony A8H', 'Philips OLED', 'Panasonic HZ2000'],
        'Smart TVs': ['Samsung Smart TV', 'LG Smart TV', 'Sony Smart TV', 'TCL Smart TV'],
        'TV Accessories': ['TV Stand', 'Cleaning Kit', 'Remote', 'Wall Mount'],
        'Smartwatches': ['Apple Watch', 'Samsung Galaxy Watch', 'Garmin Forerunner', 'Fitbit Versa'],
        'Analog Watches': ['Rolex Submariner', 'Omega Seamaster', 'Tag Heuer Carrera', 'Seiko 5'],
        'Digital Watches': ['Casio G-Shock', 'Timex Ironman', 'Garmin Fenix', 'Suunto Core'],
        'Android Tablets': ['Samsung Galaxy Tab', 'Amazon Fire', 'Lenovo Tab', 'Huawei MatePad'],
        'iPads': ['iPad Pro', 'iPad Air', 'iPad Mini', 'iPad'],
        'Windows Tablets': ['Surface Pro', 'HP Envy x2', 'Lenovo Miix', 'Dell Latitude'],
        'Refrigerators': ['LG Fridge', 'Samsung Fridge', 'Whirlpool Fridge', 'GE Fridge'],
        'Washing Machines': ['LG Washer', 'Samsung Washer', 'Whirlpool Washer', 'Bosch Washer'],
        'Microwaves': ['Panasonic Microwave', 'Samsung Microwave', 'Toshiba Microwave', 'LG Microwave'],
        'Vacuum Cleaners': ['Dyson Vacuum', 'Roomba', 'Shark Vacuum', 'Hoover Vacuum'],
        'Headphones': ['Sony WH-1000XM4', 'Bose QuietComfort', 'Sennheiser HD 650', 'Beats Studio'],
        'Speakers': ['Sonos One', 'Bose SoundLink', 'JBL Flip', 'Sony SRS'],
        'Soundbars': ['Sonos Beam', 'Bose Soundbar', 'Samsung HW-Q60T', 'Yamaha YAS-209']
    }
    product_objects = []
    for subcategory in subcategories:
        for product_name in product_data[subcategory.name]:
            product_objects.append(Product(name=product_name, subcat=subcategory, price=round(random.uniform(10.0, 1000.0), 2)))
    Product.objects.bulk_create(product_objects)
    return product_objects

def generate_customers(n=6500):
    customer_objects = [Customer(name=fake.name()) for _ in range(n)]
    Customer.objects.bulk_create(customer_objects)
    return customer_objects

def generate_regions():
    regions = ['Northeast', 'Midwest', 'South', 'West']
    region_objects = [Region(name=region) for region in regions]
    Region.objects.bulk_create(region_objects)
    return region_objects

def generate_states(regions):
    state_data = {
        'Northeast': ['Maine', 'New Hampshire', 'Vermont', 'Massachusetts', 'Rhode Island', 'Connecticut', 'New York', 'New Jersey', 'Pennsylvania'],
        'Midwest': ['Ohio', 'Indiana', 'Illinois', 'Michigan', 'Wisconsin', 'Minnesota', 'Iowa', 'Missouri', 'North Dakota', 'South Dakota', 'Nebraska', 'Kansas'],
        'South': ['Delaware', 'Maryland', 'Virginia', 'West Virginia', 'Kentucky', 'North Carolina', 'South Carolina', 'Tennessee', 'Georgia', 'Florida', 'Alabama', 'Mississippi', 'Arkansas', 'Louisiana', 'Oklahoma', 'Texas'],
        'West': ['Montana', 'Idaho', 'Wyoming', 'Colorado', 'New Mexico', 'Arizona', 'Utah', 'Nevada', 'Washington', 'Oregon', 'California', 'Alaska', 'Hawaii']
    }
    state_objects = []
    for region in regions:
        for state_name in state_data[region.name]:
            state_objects.append(State(name=state_name, region=region))
    State.objects.bulk_create(state_objects)
    return state_objects

def generate_cities(states):
    city_objects = [City(name=fake.city(), state=state) for state in states]
    City.objects.bulk_create(city_objects)
    return city_objects

def generate_orders(customers, products, cities, states, n=10000):
    orders_data = []
    for _ in range(n):
        order_date = fake.date_this_decade()
        ship_date = fake.date_between(start_date=order_date, end_date='+30d')
        customer = random.choice(customers)
        product = random.choice(products)
        city = random.choice(cities)
        state = random.choice(states)
        quantity = random.randint(1, 10)
        discount = round(random.uniform(0.0, 0.3), 2)
        sales = round(quantity * float(product.price) * (1 - discount), 2)
        profit = round(sales * random.uniform(0.1, 0.5), 2)
        postal_code = fake.zipcode()
        shipmode = random.choice(['Second Class', 'Standard Class', 'First Class', 'Same Day'])
        segment = random.choice(['Consumer', 'Corporate', 'Home Office'])
        orders_data.append(Order(
            order_date=order_date,
            customer=customer,
            product=product,
            quantity=quantity,
            sales=sales,
            discount=discount,
            profit=profit,
            ship_date=ship_date,
            city=city,
            state=state,
            postal_code=postal_code,
            shipmode=shipmode,
            segment=segment
        ))
    Order.objects.bulk_create(orders_data)
    return orders_data
```

Data is generated to be as close to realistic as possible, while still being somewhat naturally-looking. Important notes:

- In `generate_orders()` both shipmode and segment are chosen from an enum, since that's the custom data type for this column in the DB.
- `sales` are relying on `discount` to be calculated, as well as `profit` relies on `sales`.
- `random.uniform(0.1, 0.5)` in calculating `profit` is there to account for potential costs of delivery, production etc. which are not included in the generation.

### Method calls and prints

```python
categories_data = generate_categories()
print(f"Generated {len(categories_data)} categories.")
subcategories_data = generate_subcategories(categories_data)
print(f"Generated {len(subcategories_data)} subcategories.")
products_data = generate_products(subcategories_data)
print(f"Generated {len(products_data)} products.")
customers_data = generate_customers()
print(f"Generated {len(customers_data)} customers.")
regions_data = generate_regions()
print(f"Generated {len(regions_data)} regions.")
states_data = generate_states(regions_data)
print(f"Generated {len(states_data)} states.")
cities_data = generate_cities(states_data)
print(f"Generated {len(cities_data)} cities.")
orders_data = generate_orders(customers_data, products_data, cities_data, states_data)
print(f"Generated {len(orders_data)} orders.")

print("Database populated successfully!")
```

Each method call is followed by a print statement, which confirms the generated amounts.
