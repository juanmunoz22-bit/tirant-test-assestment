import datetime
from typing import List
import uuid

from pydantic import BaseModel, Field

from app.db.config import Database

class Sale(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    product_id: str
    quantity: int
    sale_date: datetime.datetime = Field(default_factory=datetime.datetime.now)

    @classmethod
    def create_table(cls):
        conn = Database.connect()
        Database.create_table(
            conn,
            "CREATE TABLE IF NOT EXISTS sales (id TEXT, product_id TEXT, quantity INTEGER, sale_date TEXT)"
        )
        Database().close_connection(conn)