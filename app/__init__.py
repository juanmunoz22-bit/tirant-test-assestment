from flask import Flask

from app.products.products_routes import products_bp

app = Flask(__name__)

app.register_blueprint(products_bp, url_prefix="/api/v1/products")