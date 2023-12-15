from app.products.products_model import Product
from app.sales.sales_model import Sale

if __name__ == "__main__":
    Product.create_table()
    Sale.create_table()