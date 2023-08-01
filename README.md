# Pytest POC (Proof of Concept)

Este repositório contém um exemplo simples de testes automatizados usando a biblioteca Pytest. O objetivo desta POC (Proof of Concept) é demonstrar como criar e executar testes de unidade para uma classe `Product` em Python.

## Pré-requisitos

Antes de executar os testes, você precisará ter o Python e o Pytest instalados no seu ambiente de desenvolvimento. Certifique-se de ter o Python 3.x instalado e, em seguida, instale o Pytest usando o gerenciador de pacotes `pip`:

```
pip install pytest
```

## Estrutura do projeto

A estrutura do projeto é organizada da seguinte forma:

```
codigo/
  ├── Product.py
tests/
  ├── test_product.py
pytest.ini
README.md
```

- A pasta `codigo` contém o arquivo `Product.py`, que implementa a classe `Product` usada nos testes.

- A pasta `testes` contém o arquivo `test_product.py`, que contém os casos de teste para a classe `Product`.

- O arquivo `pytest.ini` é usado para configurar opções específicas do pytest, como marcas, relatórios, etc.

## Executando os testes

Para executar os testes, navegue até o diretório raiz do projeto e execute o seguinte comando:

```
pytest -v
```

O pytest descobrirá e executará todos os testes no arquivo `test_product.py` e exibirá o resultado no console.

## Casos de teste

A classe `Product` representa um produto com os seguintes atributos:

- `name`: Nome do produto.
- `price`: Preço do produto.
- `stock_quantity`: Quantidade em estoque do produto.

Os seguintes casos de teste são cobertos nos testes:

1. Teste de adicionar um novo produto e validar se foi adicionado corretamente.
2. Teste de atualizar a quantidade em estoque de um produto.
3. Teste de atualizar a quantidade em estoque para um valor inválido e validar a mensagem de erro.
4. Teste de verificar se o valor total do estoque para um produto cadastrado está correto.

## Contribuição

Este é um projeto de POC e não está aberto para contribuições externas no momento.

Se você tiver alguma dúvida ou sugestão, fique à vontade para entrar em contato.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE). Sinta-se à vontade para usar e modificar conforme necessário.
