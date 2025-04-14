"""
Testes da classe Funcionario.
"""
import unittest

from funcionario import Funcionario

NOME: str = "João"
MATRICULA: int = 12345

"""Funcionário usado para testes."""
funcionario_teste = Funcionario(nome="João", matricula=12345)


class TestFuncionarioCalcularPagamento(unittest.TestCase):
    """Testa o método calcular_pagamento da classe Funcionario."""

    def test_atributos_funcionario(self):
        """Verifica se os atributos do Funcionario estão como esperado."""
        atributos_esperados = {
            "nome": NOME,
            "matricula": MATRICULA,
            "salario_hora": 100.0,
            "horas_trabalhadas": 0.0,
            "custo_empregador": 1000.0,
            "valor_comissao": 100.0,
            "contratos_fechados": 0,
        }
        for chave, valor in atributos_esperados.items():
            valor_teste = getattr(funcionario_teste, chave)
            with self.subTest(atributo=chave, esperado=valor, atual=valor_teste):
                self.assertEqual(valor, valor_teste)

    def calcular_pagamento(self, funcionario: Funcionario) -> float:
        """Calcula o pagamento esperado para um funcionário."""
        pagamento = funcionario.salario_hora * funcionario.horas_trabalhadas + funcionario.custo_empregador
        if funcionario.valor_comissao > 0:
            pagamento += funcionario.valor_comissao * funcionario.contratos_fechados
        return pagamento

    def test_pagamento_retorna_float(self):
        """Verifica se o pagamento retorna um float."""
        self.assertIsInstance(funcionario_teste.calcular_pagamento(), float)

    def test_pagamento_com_comissao(self):
        """
        Verifica se o pagamento é calculado corretamente no caso de
        10 contratos fechados e 10 horas trabalhadas.
        """
        funcionario_teste.contratos_fechados = 10
        funcionario_teste.horas_trabalhadas = 10.0
        funcionario_teste.valor_comissao = 100.0
        self.assertAlmostEqual(funcionario_teste.calcular_pagamento(), 3000.0)

    def test_pagamento_sem_comissao_sem_horas(self):
        """Verifica se o pagamento é calculado corretamente sem comissão e sem horas trabalhadas."""
        funcionario_teste.contratos_fechados = 0
        funcionario_teste.horas_trabalhadas = 0
        self.assertAlmostEqual(
            funcionario_teste.calcular_pagamento(),
            self.calcular_pagamento(funcionario_teste),
        )

    def test_pagamento_sem_comissao(self):
        """Verifica se o pagamento é calculado corretamente sem comissão e com 10 horas trabalhadas."""
        funcionario_teste.horas_trabalhadas = 10.0
        funcionario_teste.valor_comissao = 0.0
        self.assertAlmostEqual(funcionario_teste.calcular_pagamento(), 2000.0)

    def test_pagamento_comissao_desabilitada(self):
        """
        Verifica se o pagamento é calculado corretamente no caso de
        10 contratos fechados e 10 horas trabalhadas,
        mas com comissão desabilitada.
        """
        funcionario_teste.horas_trabalhadas = 10.0
        funcionario_teste.valor_comissao = 0.0
        self.assertAlmostEqual(funcionario_teste.calcular_pagamento(), 2000.0)


if __name__ == "__main__":
    unittest.main() 