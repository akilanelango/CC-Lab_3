from products import dao
from typing import List


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict):
        """Load a Product instance from a dictionary."""
        return Product(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            cost=data['cost'],
            qty=data.get('qty', 0)
        )

def list_products() -> List[Product]:
    """Retrieve a list of all products."""
    products_data = dao.list_products()
    return [Product.load(product) for product in products_data]

def get_product(product_id: int) -> Product:
    """Retrieve a single product by its ID."""
    product_data = dao.get_product(product_id)
    return Product.load(product_data) if product_data else None

def add_product(product: dict):
    """Add a new product to the database."""
    dao.add_product(product)

def update_qty(product_id: int, qty: int):
    """Update the quantity of a specific product."""
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
