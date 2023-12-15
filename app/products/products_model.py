import os
from typing import List
import uuid

from pydantic import BaseModel, Field

from app.db.config import Database

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    price: float
    stock: int

    @classmethod
    def create_table(cls):
        conn = Database.connect()
        Database.create_table(
            conn,
            "CREATE TABLE IF NOT EXISTS products (id TEXT, name TEXT, description TEXT, price INTEGER, stock REAL)"
        )
        Database().close_connection(conn)

    def save(self) -> "Product":
        conn = Database.connect()
        Database.insert(
            conn,
            sql="INSERT INTO products (id, name, description, price, stock) VALUES (?, ?, ?, ?, ?)",
            params=(self.id, self.name, self.description, self.price, self.stock)
        )
        Database().close_connection(conn)

        return self
    
    @classmethod
    def get_products(cls) -> List["Product"]:
        conn = Database.connect()
        records = Database.fetch_all(
            conn,
            sql="SELECT * FROM products"
        )
        Database().close_connection(conn)
        products = [cls(**record) for record in records]
        return products

