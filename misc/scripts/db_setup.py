from sqlalchemy import create_engine, Column, Integer, String, Numeric, Date, ForeignKey, Enum, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.dialects.postgresql import ENUM

db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': 1234,
    'database': 'your_db_name'
}
conn_str = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
engine = create_engine(conn_str)
Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subcategories = relationship('SubCategory', back_populates='category')

class SubCategory(Base):
    __tablename__ = 'subcategory'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    category = relationship('Category', back_populates='subcategories')
    products = relationship('Product', back_populates='subcategory')

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subcat_id = Column(Integer, ForeignKey('subcategory.id'), nullable=False)
    price = Column(Numeric, nullable=False)
    subcategory = relationship('SubCategory', back_populates='products')
    orders = relationship('Order', back_populates='product')

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    orders = relationship('Order', back_populates='customer')

class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    states = relationship('State', back_populates='region')

class State(Base):
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)
    region = relationship('Region', back_populates='states')
    cities = relationship('City', back_populates='state')

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
    state = relationship('State', back_populates='cities')
    orders = relationship('Order', back_populates='city')

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
    customer = relationship('Customer', back_populates='orders')
    product = relationship('Product', back_populates='orders')
    city = relationship('City', back_populates='orders')
    state = relationship('State', back_populates='orders')

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    role_name = Column(String, nullable=False)
    role_desc = Column(String, nullable=False)
    users = relationship('User', back_populates='role')

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(Date, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    role = relationship('Role', back_populates='users')

Base.metadata.create_all(engine)

print("Schema created successfully!")
