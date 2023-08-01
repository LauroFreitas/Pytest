from codigo.Product import Product
from pytest import mark,fixture
 

@fixture
def novoProduto_Fixture():
    novoProduto = Product('Nome', 100, 1)
    return novoProduto


@mark.parametrize(
    'nome, price, stock_quantity',
    [
        # Arrange
        ('Calça', 150, 5),('Sapato', 300, 3),('Blusa', 78, 20),

    ]
)
def test_adiciona_três_novos_produtos_valida_se_os_produtos_foram_adicionados_corretamente(nome, price, stock_quantity):
    # Act
    novoProduto = Product(nome, price, stock_quantity)
   
    # Assert
    assert novoProduto.name == nome
    assert novoProduto.price == price
    assert novoProduto.stock_quantity == stock_quantity
    
  
def test_cenário_de_adição_de_produtos_ao_estoque_incluir_um_valor_inicial_e_modificar_para_3_e_validar_mensagem(novoProduto_Fixture):
    # Arrange
    resultado = novoProduto_Fixture.update_stock(3)
    
    # Act
    mensagem_esperada = f"A quantidade em estoque do produto '{novoProduto_Fixture.name}' foi atualizada para {novoProduto_Fixture.stock_quantity} unidades."
    
    # Assert
    assert mensagem_esperada in resultado
    assert novoProduto_Fixture.stock_quantity == 3

def test_cenário_de_adição_inválida_de_produtos_ao_estoque_incluir_um_valor_inicial_e_modificar_para_um_valor_invalido(novoProduto_Fixture):
    # Arrange
    resultado = novoProduto_Fixture.update_stock(-1)
    
    # Act
    mensagem_esperada = f"O estoque do produto '{novoProduto_Fixture.name}' está negativo. Verifique o estoque!"
    
    # Assert
    assert mensagem_esperada in resultado
    assert novoProduto_Fixture.stock_quantity == 1

def test_verifica_promoção_para_produto_com_oferta(novoProduto_Fixture):
   # Arrange
    novoProduto_Fixture.apply_discount(10)
    novaOferta = novoProduto_Fixture.price

    # Act
    novoProduto_Fixture.price = novaOferta

    # Assert
    assert novaOferta == 90, f"O preço com desconto ficou {novaOferta}"


@mark.parametrize(
    'stock_quantity, valor_esperado_no_estoque',
    [
        (4, 400),  
        (6, 600),   
        (8, 800),   
    ]
)
def test_verifica_valor_total_no_estoque_para_produto_cadastrado(stock_quantity, valor_esperado_no_estoque, novoProduto_Fixture):
    # Act 
    novoProduto_Fixture.stock_quantity = stock_quantity
    valorTotalEstoque = novoProduto_Fixture.get_total_value()

    # Assert
    assert valorTotalEstoque == valor_esperado_no_estoque