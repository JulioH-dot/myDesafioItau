import json
from produtos import get_product, get_all_products

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
