
## Documentação da API
#### Esta é a documentação da API que gerencia produtos.

## URLs de acesso
O mydesafioItau é uma API com propósitos de testar conhecimentos.

Foi utlizado uma lambda para validar o token e uma para processar as requests. Além de um API Gateway para receber as solicitações.

Utilizei essa arquitetura pois, é uma arquitetura de microsserviço. Sendo assim visando melhorar custos e diminuir o esforço para construção da infra.


<img align="center" height="400" width="700" alt="css-icon" src="arquitetura.jpeg">

Para testar a API, abra o Postman ou insominia e coloque o header necessário para autenticação e faça sua request

URL: https://6y6d1o9m8b.execute-api.sa-east-1.amazonaws.com/items

Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJFZmZlY3QiOiJBbGxvdyJ9.A8cfMGlfnzXnIXPI7EI_2kZqf5EtH8whOKqidhxI4y8

## Métodos
Requisições para a API devem seguir os padrões:
| Método | Descrição |
|---|---|
| `GET` | Retorna informações de um ou mais registros. |

Autorização
Para acessar esta rota, você precisa fornecer um token JWT no cabeçalho `authorization`.

## Respostas

| Código | Descrição |
|---|---|
| `200` | Requisição executada com sucesso (success).|
| `404` | Registro pesquisado não encontrado (Product not found).|
| `401` | Dados de acesso inválidos (Unauthorized).|

## Lambda Functions
A API usa um função lambda para processar as solicitações:

`get_all_products`: Consulta todos os produtos disponíveis.

`get_product_by_id`: Consulta um produto específico com base no ID fornecido..

## Autorização:

A autorização para acessar as rotas é feita através de uma lambda de autorização associada à rota do API Gateway. Esta lambda valida o token JWT fornecido no cabeçalho `authorization` da solicitação.

## Exemplos

### get_all_products 


```http
  GET /api/items
```

| Parâmetro Header   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `authorization` | `string` | **Obrigatório**. O Token da sua API |

+ Response 200 (application/json)

    + Body

            [
              {'id': 1, 'brand': 'Samsung', 'model': 'Galaxy S21', 'price': 4999.99, 'stock': 100, 'category': 'Smartphones',},
              {'id': 2, 'brand': 'Dell', 'model': 'Inspiron 15', 'price': 3499.99, 'stock': 50, 'category': 'Computadores',},
              {'id': 3, 'brand': 'Apple', 'model': 'Watch Series 6', 'price': 1999.99, 'stock': 75, 'category': 'Smartwatches',},
              {'id': 4, 'brand': 'LG', 'model': 'OLED 55"', 'price': 4499.99, 'stock': 30, 'category': 'Smart TVs',},
              ...
            ]

+ Response 401 (application/json)

    + Body

            {
                "message": "Unauthorized"
            }


### get_product_by_id

```http
  GET /api/items/${id}
```

| Parâmetro vi URL   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

| Parâmetro Header   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `authorization` | `string` | **Obrigatório**. O Token da sua API |

+ Response 200 (application/json)

    + Body
          
            {
                "id": 11,
                "brand": "Corsair",
                "model": "K95 RGB Platinum",
                "price": 999.99,
                "stock": 15,
                "category": "Teclados"
            }
            

+ Response 404 (application/json)

    + Body

            {
                "mensagem": "Product not found"
            }
            

+ Response 401 (application/json)

    + Body

            {
                "message": "Unauthorized"
            }


## Demonstração

<img align="left" height="300" width="700" alt="coding-time" src="gifReadme.gif">


