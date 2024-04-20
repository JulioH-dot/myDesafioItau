import json

products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.0},
    {'id': 2, 'name': 'Product 2', 'price': 20.0},
    {'id': 3, 'name': 'Product 3', 'price': 30.0}
]

def get_product_by_id(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        raise Exception('Product not found')
    return product

def get_all_products():
    return products
