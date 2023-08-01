from codigo.Product import Product
from pytest import mark

@mark.parametrize(
    'nome',
    [('Teste'), ('Teste2')]
)
def test_adiciona_um_produto_novo_valida_se_produto_vou_adicionado_corretamente(nome):
  novoProduto = Product(nome,100,2)
  assert novoProduto.name == nome
  assert novoProduto.price == 100
  assert novoProduto.stock_quantity == 2
  

def test_cenário_de_adição_de_produtos_ao_estoque_incluir_um_valor_inicial_e_modificar_para_3_e_validar_mensagem():
  novoProduto = Product('Chanell',50, 2)
  assert novoProduto.update_stock(3) == (f"A quantidade em estoque do produto '{novoProduto.name}' foi atualizada para {novoProduto.stock_quantity} unidades.")
  assert novoProduto.stock_quantity == 3



def test_cenário_de_adição_inválida_de_produtos_ao_estoque_incluir_um_valor_inicial_e_modificar_para_um_valor_invalido():
    novoProduto = Product('Chanell', 50, 2)
    assert novoProduto.update_stock(-1) == (f"O estoque do produto '{novoProduto.name}' está negativo. Verifique o estoque!")
    assert novoProduto.stock_quantity == 2