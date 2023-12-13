import uuid, datetime

from pydantic import BaseModel

from app.models.products_model import Product

class Sale(BaseModel):
    id: uuid.UUID
    product_id: Product
    quantity: int
    sale_date: datetime.datetime


    @classmethod
    def create(cls, product_id, quantity):
        sale = cls(
            id=uuid.uuid4(),
            product_id=product_id,
            quantity=quantity,
            sale_date=datetime.datetime.now() 
        )

        return sale