
## Documentação da API
#### Esta é a documentação da API que gerencia produtos.

## URLs de acesso

O MyDesafioItau foi desenvolvido como uma API para avaliar competências em arquitetura e desenvolvimento em nuvem AWS.

O uso de funções Lambda para autenticar o token e processar as requisições permite uma abordagem mais flexível e eficiente em termos de custos, pois as funções são executadas apenas quando necessário, escalando automaticamente de acordo com a demanda. Além disso, as funções Lambda são gerenciadas pela AWS, o que reduz a carga operacional e simplifica o gerenciamento da infraestrutura.

O API Gateway atua como ponto de entrada para a API, gerenciando as solicitações de forma segura e fornecendo funcionalidades como autorização e monitoramento dos endpoints. Isso contribui para a segurança da aplicação, garantindo que apenas solicitações válidas sejam processadas e permitindo o controle fino sobre as permissões de acesso.

Essa arquitetura baseada em microsserviços não só melhora a eficiência e reduz os custos operacionais, mas também torna o sistema mais resiliente e tolerante a falhas, pois cada microsserviço pode ser desenvolvido, implantado e escalado de forma independente. Isso significa que uma falha em um microsserviço não afetará necessariamente o funcionamento de todo o sistema, aumentando a confiabilidade e a disponibilidade da aplicação. Deixando claro que pode ser adicionado mais métodos de requisições como POST, PUT e DELETE conforme os conceitos REST cada um com seu microsserviço específico.


<img align="center" height="700" width="700" alt="css-icon" src="architeture.png">

Para testar a API, abra o Postman ou insominia e coloque o header necessário para autenticação e faça sua request

URL: https://6y6d1o9m8b.execute-api.sa-east-1.amazonaws.com/items

Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJFZmZlY3QiOiJBbGxvdyJ9.A8cfMGlfnzXnIXPI7EI_2kZqf5EtH8whOKqidhxI4y8

## Métodos
Requisições para a API devem seguir os padrões:
| Método | Descrição |
|---|---|
| `GET` | Retorna informações de um ou mais registros. |

Autorização
Para acessar esta rota, você precisa fornecer um token JWT no cabeçalho `Authorization`.

## Respostas

| Código | Descrição |
|---|---|
| `200` | Requisição executada com sucesso (success).|
| `404` | Registro pesquisado não encontrado (Product not found).|
| `401` | Falta de dados de acesso (Unauthorized).|
| `403` | Dados de acesso inválidos (Forbidden).|

## Lambda Functions
A API usa um função lambda para processar as solicitações:

`get_all_products`: Consulta todos os produtos disponíveis.

`get_product_by_id`: Consulta um produto específico com base no ID fornecido..

## Autorização:

A autorização para acessar as rotas é feita através de uma lambda de autorização associada à rota do API Gateway. Esta lambda valida o token JWT fornecido no cabeçalho `Authorization` da solicitação.

## Exemplos

### get_all_products 


```http
  GET /api/items
```

| Parâmetro Header   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `Authorization` | `string` | **Obrigatório**. O Token da sua API |

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

+ Response 403 (application/json)

    + Body

            {
                "message": "Forbidden"
            }


### get_product_by_id

```http
  GET /api/items/${id}
```

| Parâmetro via URL   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

| Parâmetro Header   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `Authorization` | `string` | **Obrigatório**. O Token da sua API |

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

+ Response 403 (application/json)

    + Body

            {
                "message": "Forbidden"
            }



