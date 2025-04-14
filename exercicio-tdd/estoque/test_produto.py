"""
Testes da classe Produto.
"""
import unittest
from datetime import datetime, timedelta

from produto import Produto


class TestProduto(unittest.TestCase):
    """Testa a classe Produto."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.produto = Produto(
            codigo="P001",
            nome="Arroz",
            preco=25.90,
            quantidade=50,
            data_validade=datetime.now() + timedelta(days=365),
            estoque_minimo=10
        )

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        self.assertEqual(self.produto.codigo, "P001")
        self.assertEqual(self.produto.nome, "Arroz")
        self.assertEqual(self.produto.preco, 25.90)
        self.assertEqual(self.produto.quantidade, 50)
        self.assertEqual(self.produto.estoque_minimo, 10)

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente."""
        self.produto.adicionar_estoque(30)
        self.assertEqual(self.produto.quantidade, 80)

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        # Teste com quantidade suficiente
        sucesso = self.produto.remover_estoque(20)
        self.assertTrue(sucesso)
        self.assertEqual(self.produto.quantidade, 30)
        
        # Teste com quantidade insuficiente
        sucesso = self.produto.remover_estoque(40)
        self.assertFalse(sucesso)
        self.assertEqual(self.produto.quantidade, 30)

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        # Teste com estoque acima do mínimo
        self.assertFalse(self.produto.verificar_estoque_baixo())
        
        # Teste com estoque abaixo do mínimo
        self.produto.quantidade = 5
        self.assertTrue(self.produto.verificar_estoque_baixo())

    def test_calcular_valor_total(self):
        """Verifica se o valor total é calculado corretamente."""
        valor_total = self.produto.calcular_valor_total()
        self.assertAlmostEqual(valor_total, 1295.0)  # 50 * 25.90

    def test_verificar_validade(self):
        """Verifica se a validação de data de validade funciona corretamente."""
        # Teste com produto dentro da validade
        self.assertTrue(self.produto.verificar_validade())
        
        # Teste com produto fora da validade
        self.produto.data_validade = datetime.now() - timedelta(days=1)
        self.assertFalse(self.produto.verificar_validade())
        
        # Teste com produto sem data de validade
        self.produto.data_validade = None
        self.assertTrue(self.produto.verificar_validade())


if __name__ == "__main__":
    unittest.main() 