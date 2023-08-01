from codigo.Product import Product
from pytest import mark,fixture
 

@fixture
def novoProduto_Fixture():
    novoProduto = Product('Nome', 100, 1)
    return novoProduto


@mark.parametrize(
    'nome, price, stock_quantity',
    [
        ('Teste', 100, 2),
        ('Teste2', 200, 5),
        ('Teste3', 0, 10),
    ]
)
def test_adiciona_três_novos_produtos_valida_se_os_produtos_foram_adicionados_corretamente(nome, price, stock_quantity):
    novoProduto = Product(nome, price, stock_quantity)
    assert novoProduto.name == nome
    assert novoProduto.price == price
    assert novoProduto.stock_quantity == stock_quantity
    
  

def test_cenário_de_adição_de_produtos_ao_estoque_incluir_um_valor_inicial_e_modificar_para_3_e_validar_mensagem(novoProduto_Fixture):
  assert novoProduto_Fixture.update_stock(3) == (f"A quantidade em estoque do produto '{novoProduto_Fixture.name}' foi atualizada para {novoProduto_Fixture.stock_quantity} unidades.")
  assert novoProduto_Fixture.stock_quantity == 3



def test_cenário_de_adição_inválida_de_produtos_ao_estoque_incluir_um_valor_inicial_e_modificar_para_um_valor_invalido(novoProduto_Fixture):
    assert novoProduto_Fixture.update_stock(-1) == (f"O estoque do produto '{novoProduto_Fixture.name}' está negativo. Verifique o estoque!")
    assert novoProduto_Fixture.stock_quantity == 1

def test_verifica_se_o_produto_está_em_promoção_com_base_no_preço_fornecido():
   ...