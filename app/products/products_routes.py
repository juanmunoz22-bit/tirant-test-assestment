import json

from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from app.products.products_service import CreateProductCommand, ListProductsQuery

products_bp = Blueprint("products", __name__)

@products_bp.route("/", methods=["POST"])
def create():
    cmd = CreateProductCommand(**request.json)
    product = cmd.execute()
    return product.model_dump(), 201

@products_bp.route("/", methods=["GET"])
def list_products():
    query = ListProductsQuery()
    products = query.execute()
    return [product.model_dump(exclude=["id"]) for product in products], 200

@products_bp.errorhandler(ValidationError)
def handle_validation_exception(error):
    response = jsonify(error.errors())
    response.status_code = 400
    return response
