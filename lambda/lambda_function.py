import json

def lambda_handler(event, context):
    
    path_params = event.get('pathParameters')
    if path_params and 'id' in path_params:
        try:
            product_id = int(path_params['id'])
            product = get_product_by_id(product_id)
            return gerar_resposta(status_code=200, response=product)
        except Exception as e:
            return gerar_resposta(status_code=404, mensagem=str(e))
    else:
        return gerar_resposta(status_code=200, response=get_all_products())

def gerar_resposta(status_code: int, mensagem: str = None, response: dict = None):
    headers = {
        'Access-Control-Allow-Headers': '*',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Method': '*'
    } 

    if mensagem:
        body = {'mensagem': mensagem}
    elif response:
        body = response
    else:
        body = {}

    return {
        'statusCode': status_code,
        'headers': headers,
        'body': json.dumps(body, default=str, ensure_ascii=False)
    }

def get_product_by_id(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        raise Exception('Product not found')
    return product

def get_all_products():
    return products

products = [
    {'id': 1, 'brand': 'Samsung', 'model': 'Galaxy S21', 'price': 4999.99, 'stock': 100, 'category': 'Smartphones',},
    {'id': 2, 'brand': 'Dell', 'model': 'Inspiron 15', 'price': 3499.99, 'stock': 50, 'category': 'Computadores',},
    {'id': 3, 'brand': 'Apple', 'model': 'Watch Series 6', 'price': 1999.99, 'stock': 75, 'category': 'Smartwatches',},
    {'id': 4, 'brand': 'LG', 'model': 'OLED 55"', 'price': 4499.99, 'stock': 30, 'category': 'Smart TVs',},
    {'id': 5, 'brand': 'Samsung', 'model': 'Galaxy Tab S7', 'price': 2999.99, 'stock': 60, 'category': 'Tablets',},
    {'id': 6, 'brand': 'Canon', 'model': 'EOS Rebel T7i', 'price': 2999.99, 'stock': 25, 'category': 'Câmeras',},
    {'id': 7, 'brand': 'Sony', 'model': 'Playstation 5', 'price': 4999.99, 'stock': 20, 'category': 'Consoles',},
    {'id': 8, 'brand': 'Apple', 'model': 'AirPods Pro', 'price': 1499.99, 'stock': 50, 'category': 'Fones de Ouvido',},
    {'id': 9, 'brand': 'ASUS', 'model': '27"', 'price': 1999.99, 'stock': 40, 'category': 'Monitores',},
    {'id': 10, 'brand': 'HP', 'model': 'DeskJet 2776', 'price': 299.99, 'stock': 70, 'category': 'Impressoras'},
    {'id': 11, 'brand': 'Corsair', 'model': 'K95 RGB Platinum', 'price': 999.99, 'stock': 15, 'category': 'Teclados'},
    {'id': 12, 'brand': 'Logitech', 'model': 'G502 HERO', 'price': 399.99, 'stock': 35, 'category': 'Mouses'},
    {'id': 13, 'brand': 'TP-Link', 'model': 'Archer C6', 'price': 299.99, 'stock': 45, 'category': 'Roteadores'},
    {'id': 14, 'brand': 'JBL', 'model': 'Charge 4', 'price': 799.99, 'stock': 25, 'category': 'Caixas de Som'},
    {'id': 15, 'brand': 'Blue', 'model': 'Yeti', 'price': 799.99, 'stock': 20, 'category': 'Microfones'},
    {'id': 16, 'brand': 'Seagate', 'model': 'Expansion 1TB', 'price': 399.99, 'stock': 50, 'category': 'HDs Externos'},
    {'id': 17, 'brand': 'DXRacer', 'model': 'Gamer', 'price': 1999.99, 'stock': 10, 'category': 'Cadeiras'},
    {'id': 18, 'brand': 'Dell', 'model': 'Essential', 'price': 149.99, 'stock': 30, 'category': 'Mochilas'},
    {'id': 19, 'brand': 'LED', 'model': 'Mesa', 'price': 79.99, 'stock': 40, 'category': 'Luminárias'},
    {'id': 20, 'brand': 'Mondial', 'model': 'Mesa', 'price': 149.99, 'stock': 55, 'category': 'Ventiladores'},
    {'id': 21, 'brand': 'Consul', 'model': '120L', 'price': 999.99, 'stock': 15, 'category': 'Frigobares'},
    {'id': 22, 'brand': 'Philco', 'model': 'Pressão Elétrica', 'price': 299.99, 'stock': 25, 'category': 'Panelas de Pressão'},
    {'id': 23, 'brand': 'Oster', 'model': '450W', 'price': 199.99, 'stock': 30, 'category': 'Liquidificadores'},
    {'id': 24, 'brand': 'Fischer', 'model': 'Elétrico', 'price': 399.99, 'stock': 20, 'category': 'Fornos'},
    {'id': 25, 'brand': 'Electrolux', 'model': 'EasyBox', 'price': 499.99, 'stock': 10, 'category': 'Aspiradores de Pó'},
    {'id': 26, 'brand': 'Brastemp', 'model': '11kg', 'price': 1999.99, 'stock': 5, 'category': 'Máquinas de Lavar'},
    {'id': 27, 'brand': 'Mueller', 'model': 'Roupas', 'price': 1499.99, 'stock': 8, 'category': 'Secadoras'},
    {'id': 28, 'brand': 'Gamer', 'model': 'Retrátil e Reclinável', 'price': 2999.99, 'stock': 12, 'category': 'Sofás'},
    {'id': 29, 'brand': 'Queen Size', 'model': 'Cama Box', 'price': 999.99, 'stock': 20, 'category': 'Camas'},
    {'id': 30, 'brand': 'Casal', 'model': '3 Portas', 'price': 799.99, 'stock': 15, 'category': 'Guarda-Roupas'}
]
