"""
Testes da classe Funcionario.
"""
import unittest

from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""

    def test_calcular_salario_bruto(self):
        """Testa o cálculo do salário bruto."""
        funcionario = Funcionario(
            nome="João",
            matricula=123,
            salario_hora=50.0,
            horas_trabalhadas=160
        )
        self.assertEqual(funcionario.calcular_salario_bruto(), 8000.0)

    def test_calcular_comissao(self):
        """Testa o cálculo da comissão."""
        funcionario_com_comissao = Funcionario(
            nome="Maria",
            matricula=456,
            tem_comissao=True,
            valor_comissao=200.0,
            contratos_fechados=5
        )
        self.assertEqual(funcionario_com_comissao.calcular_comissao(), 1000.0)

        funcionario_sem_comissao = Funcionario(
            nome="Carlos",
            matricula=789,
            tem_comissao=False,
            valor_comissao=200.0,
            contratos_fechados=5
        )
        self.assertEqual(funcionario_sem_comissao.calcular_comissao(), 0.0)

    def test_calcular_custo_total(self):
        """Testa o cálculo do custo total."""
        funcionario = Funcionario(
            nome="Ana",
            matricula=321,
            salario_hora=60.0,
            horas_trabalhadas=100,
            custo_empregador=1500.0,
            tem_comissao=True,
            valor_comissao=150.0,
            contratos_fechados=3
        )
        salario = 60.0 * 100  # 6000
        comissao = 150.0 * 3  # 450
        custo_total = salario + 1500.0 + comissao
        self.assertEqual(funcionario.calcular_custo_total(), custo_total)


if __name__ == "__main__":
    unittest.main()
git push origin main
