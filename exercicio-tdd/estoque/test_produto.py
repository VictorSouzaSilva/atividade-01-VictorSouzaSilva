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
        self.produto = Produto(codigo="001", nome="Produto Teste", preco=10.0)

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        self.assertEqual(self.produto.codigo, "001")
        self.assertEqual(self.produto.nome, "Produto Teste")
        self.assertEqual(self.produto.preco, 10.0)
        self.assertEqual(self.produto.quantidade, 0)

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente."""
        self.produto.adicionar_estoque(5)
        self.assertEqual(self.produto.quantidade, 5)

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        self.produto.adicionar_estoque(10)
        resultado = self.produto.remover_estoque(5)
        self.assertTrue(resultado)
        self.assertEqual(self.produto.quantidade, 5)

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        self.produto.adicionar_estoque(5)
        self.assertTrue(self.produto.verificar_estoque_baixo())
        self.produto.adicionar_estoque(10)
        self.assertFalse(self.produto.verificar_estoque_baixo())

    def test_calcular_valor_total(self):
        """Verifica se o valor total é calculado corretamente."""
        self.produto.adicionar_estoque(10)
        self.assertEqual(self.produto.calcular_valor_total(), 100.0)

    def test_verificar_validade(self):
        """Verifica se a validação de data de validade funciona corretamente."""
        produto_valido = Produto(codigo="002", nome="Produto com validade", preco=10.0, data_validade=datetime.now() + timedelta(days=1))
        self.assertTrue(produto_valido.verificar_validade())
        
        produto_invalidado = Produto(codigo="003", nome="Produto vencido", preco=10.0, data_validade=datetime.now() - timedelta(days=1))
        self.assertFalse(produto_invalidado.verificar_validade())