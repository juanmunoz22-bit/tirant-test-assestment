from typing import List

from pydantic import BaseModel

from app.products.products_model import Product

class CreateProductCommand(BaseModel):
    
    name: str
    description: str
    price: float
    stock: int

    def execute(self) -> Product:
        product = Product(
            name=self.name,
            description=self.description,
            price=self.price,
            stock=self.stock
        ).save()

        return product
    
class ListProductsQuery(BaseModel):
    
    def execute(self) -> List[Product]:
        products = Product.get_products()

        return products
