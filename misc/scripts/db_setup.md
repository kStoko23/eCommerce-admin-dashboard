# E-commerce Mock DB

This script generates DB scheme used in this project

## Installation

1. Clone the repository.
2. Install the required Python packages:

   ```sh
   pip install sqlalchemy faker
   ```

3. Set up your PostgreSQL database and update the `db_config` in `db_setup.py` with your database credentials.

## Usage

Run the data generator script:

```sh
python db_setup.py
```

## Code Overview

### Module Imports

```python
from sqlalchemy import create_engine, Column, Integer, String, Numeric, Date, ForeignKey, Enum, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.dialects.postgresql import ENUM
```

These modules are used for generating test data (Faker), working with the database (SQLAlchemy), and handling date and time (datetime).

### Database Configuration

```python
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
```

This section sets up the connection to the PostgreSQL database using SQLAlchemy and initializes the Faker library for generating fake data.

## Model Definitions

### Category Model

```python

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
```

Represents a product category with attributes:

    id: Unique identifier for the category.
    name: Name of the category.

### SubCategory Model

```python

class SubCategory(Base):
    __tablename__ = 'subcategory'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    category = relationship("Category", back_populates="subcategories")
```

Represents a product subcategory with attributes:

    id: Unique identifier for the subcategory.
    name: Name of the subcategory.
    category_id: Identifier of the parent category.

### Product Model

```python

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subcat_id = Column(Integer, ForeignKey('subcategory.id'), nullable=False)
    price = Column(Numeric, nullable=False)
    subcategory = relationship("SubCategory", back_populates="products")
```

Represents a product with attributes:

    id: Unique identifier for the product.
    name: Name of the product.
    subcat_id: Identifier of the subcategory.
    price: Price of the product.

### Customer Model

```python

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
```

Represents a customer with attributes:

    id: Unique identifier for the customer.
    name: Name of the customer.

### Region Model

```python

class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
```

Represents a geographic region with attributes:

    id: Unique identifier for the region.
    name: Name of the region.

### State Model

```python

class State(Base):
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)
    region = relationship("Region", back_populates="states")
```

Represents a state within a region with attributes:

    id: Unique identifier for the state.
    name: Name of the state.
    region_id: Identifier of the parent region.

### City Model

```python

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
    state = relationship("State", back_populates="cities")
```

Represents a city within a state with attributes:

    id: Unique identifier for the city.
    name: Name of the city.
    state_id: Identifier of the parent state.

### Order Model

```python
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
```

Represents an order with attributes:

    id: Unique identifier for the order.
    order_date: Date of the order.
    customer_id: Identifier of the customer who placed the order.
    product_id: Identifier of the product ordered.
    quantity: Quantity of the product ordered.
    sales: Total sales amount for the order.
    discount: Discount applied to the order.
    profit: Profit from the order.
    ship_date: Shipping date of the order.
    city_id: Identifier of the city where the order was shipped.
    state_id: Identifier of the state where the order was shipped.
    postal_code: Postal code for the order.
    shipmode: Shipping mode for the order.
    segment: Customer segment for the order.

### Relationships

```python
Category.subcategories = relationship("SubCategory", order_by=SubCategory.id, back_populates="category")
SubCategory.products = relationship("Product", order_by=Product.id, back_populates="subcategory")
Region.states = relationship("State", order_by=State.id, back_populates="region")
State.cities = relationship("City", order_by=City.id, back_populates="state")
```

Defines relationships between models.

### Create Tables in the Database

```python
Base.metadata.create_all(engine)
print("Schema created successfully!")
```

Creates tables in the database based on the defined models.
