import random
from faker import Faker
from sqlalchemy import create_engine, Table, Column, Integer, String, Numeric, Date, MetaData, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': 1234,
    'database': 'your_db_name'
}
conn_str = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
engine = create_engine(conn_str)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
fake = Faker()

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class SubCategory(Base):
    __tablename__ = 'subcategory'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    category = relationship("Category", back_populates="subcategories")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subcat_id = Column(Integer, ForeignKey('subcategory.id'), nullable=False)
    price = Column(Numeric, nullable=False)
    subcategory = relationship("SubCategory", back_populates="products")

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class State(Base):
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)
    region = relationship("Region", back_populates="states")

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
    state = relationship("State", back_populates="cities")

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    order_date = Column(Date, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    sales = Column(Numeric, nullable=False)
    discount = Column(Numeric, nullable=False)
    profit = Column(Numeric, nullable=False)
    ship_date = Column(Date, nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
    postal_code = Column(Integer, nullable=False)
    shipmode = Column(ENUM('Second Class', 'Standard Class', 'First Class', 'Same Day', name='shipmode_enum'))
    segment = Column(ENUM('Consumer', 'Corporate', 'Home Office', name='segment_enum'))

Category.subcategories = relationship("SubCategory", order_by=SubCategory.id, back_populates="category")
SubCategory.products = relationship("Product", order_by=Product.id, back_populates="subcategory")
Region.states = relationship("State", order_by=State.id, back_populates="region")
State.cities = relationship("City", order_by=City.id, back_populates="state")

Base.metadata.create_all(engine)

category_data = {
    'Computers': ['Laptops', 'Desktops', 'Components', 'Peripherals'],
    'Phones': ['Smartphones', 'Landline Phones', 'Phone Accessories'],
    'TV': ['LED TVs', 'OLED TVs', 'Smart TVs', 'TV Accessories'],
    'Watches': ['Smartwatches', 'Analog Watches', 'Digital Watches'],
    'Tablets': ['Android Tablets', 'iPads', 'Windows Tablets'],
    'Home Appliances': ['Refrigerators', 'Washing Machines', 'Microwaves', 'Vacuum Cleaners'],
    'Audio': ['Headphones', 'Speakers', 'Soundbars']
}

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

def generate_categories():
    return [Category(name=category) for category in category_data.keys()]

def generate_subcategories(categories):
    subcategories_data = []
    for category in categories:
        subcategories = category_data[category.name]
        subcategories_data.extend([SubCategory(name=subcat, category=category) for subcat in subcategories])
    return subcategories_data

def generate_products(subcategories):
    products_data = []
    for subcategory in subcategories:
        products = product_data[subcategory.name]
        products_data.extend([Product(name=product, subcategory=subcategory, price=round(random.uniform(10.0, 1000.0), 2)) for product in products])
    return products_data

def generate_customers(n=6500):
    return [Customer(name=fake.name()) for _ in range(n)]

def generate_regions():
    return [Region(name=region) for region in ['Northeast', 'Midwest', 'South', 'West']]

def generate_states(regions):
    states = {
        'Northeast': ['Maine', 'New Hampshire', 'Vermont', 'Massachusetts', 'Rhode Island', 'Connecticut', 'New York', 'New Jersey', 'Pennsylvania'],
        'Midwest': ['Ohio', 'Indiana', 'Illinois', 'Michigan', 'Wisconsin', 'Minnesota', 'Iowa', 'Missouri', 'North Dakota', 'South Dakota', 'Nebraska', 'Kansas'],
        'South': ['Delaware', 'Maryland', 'Virginia', 'West Virginia', 'Kentucky', 'North Carolina', 'South Carolina', 'Tennessee', 'Georgia', 'Florida', 'Alabama', 'Mississippi', 'Arkansas', 'Louisiana', 'Oklahoma', 'Texas'],
        'West': ['Montana', 'Idaho', 'Wyoming', 'Colorado', 'New Mexico', 'Arizona', 'Utah', 'Nevada', 'Washington', 'Oregon', 'California', 'Alaska', 'Hawaii']
    }
    state_data = []
    for region in regions:
        state_data.extend([State(name=state, region=region) for state in states[region.name]])
    return state_data

def generate_cities(states):
    return [City(name=fake.city(), state=state) for state in states]

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
        sales = round(quantity * product.price * (1 - discount), 2)
        profit = round(sales * random.uniform(0.1, 0.5), 2)
        postal_code = fake.zipcode()
        shipmode = random.choice(['Second Class', 'Standard Class', 'First Class', 'Same Day'])
        segment = random.choice(['Consumer', 'Corporate', 'Home Office'])
        orders_data.append(Order(
            order_date=order_date,
            customer_id=customer.id,
            product_id=product.id,
            quantity=quantity,
            sales=sales,
            discount=discount,
            profit=profit,
            ship_date=ship_date,
            city_id=city.id,
            state_id=state.id,
            postal_code=postal_code,
            shipmode=shipmode,
            segment=segment
        ))
    return orders_data




categories_data = generate_categories()
subcategories_data = generate_subcategories(categories_data)
products_data = generate_products(subcategories_data)
customers_data = generate_customers()
regions_data = generate_regions()
states_data = generate_states(regions_data)
cities_data = generate_cities(states_data)
orders_data = generate_orders(customers_data, products_data, cities_data, states_data)

def insert_data(session, data):
    session.add_all(data)
    session.commit()

Session = sessionmaker(bind=engine)
session = Session()

insert_data(session, categories_data)
insert_data(session, subcategories_data)
insert_data(session, products_data)
insert_data(session, customers_data)
insert_data(session, regions_data)
insert_data(session, states_data)
insert_data(session, cities_data)
insert_data(session, orders_data)

print("Database populated successfully!")