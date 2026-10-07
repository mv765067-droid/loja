def test_soma_preco_vezes_quantidade():
    # 1. preparar
     itens = [(39.90, 3), (129.90, 1)]
     # 2. agir
total = total_carrinho(itens)
    # 3. conferir
assert total == pytest.approx(249.60)
import pytest
from loja.calculos import total_carrinho
def test_carrinho_vazio_custa_zero():
    assert total_carrinho([]) == 0
    test_soma_preco_vezes_quantidade()
     # 1. preparar
    itens = [(39.90, 3), (129.90, 1)]
      # 2. agir
    total = total_carrinho(itens)
      # 3. conferir
    assert total == pytest.approx(249.60) 
    def test_tres_camisetas():
     assert total_carrinho([(39.90, 3)]) == 119.70
    pytest
F
E       
assert total_carrinho([(39.90, 3)]) == 119.70
assert 119.69999999999999 == 119.7

total = total + preco + quantidade   # era *


pytest
E       
assert 173.8 == 249.6 + 2.5e-04
E         
E         
Obtained: 173.8
Expected: 249.6 + 2.5e-04
def test_frete_abaixo_de_200_custa_15():
   assert frete(199.99) == 15.0
   def test_frete_a_partir_de_200_e_gratis():
    assert frete(200.00) == 0.0
    assert frete(350.00) == 0.0


    FRETE_FIXO = 15.0
FRETE_GRATIS_A_PARTIR_DE = 200.0
def frete(valor_da_compra):
 """Frete grátis a partir de R$ 200; abaixo disso, R$ 15."""
if valor_da_compra >= FRETE_GRATIS_A_PARTIR_DE:
    return 0.0
  return FRETE_FIXO