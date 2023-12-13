import uuid

from pydantic import BaseModel

class Product(BaseModel):
    id: uuid.UUID
    name: str
    description: str
    price: float
    stock: int

    @classmethod
    def create(cls, name, description, price, stock):
        product = cls(
            id=uuid.uuid4(),
            name=name,
            description=description,
            price=price,
            stock=stock
        )

        return product