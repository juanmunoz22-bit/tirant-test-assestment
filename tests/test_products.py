from app.models.products_model import Product

def test_create_product():
    product = Product.create(
        name="Product 1",
        description="Desc",
        price=1.10,
        stock=10,
    )

    assert product.price == 1.10