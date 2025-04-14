"""
Testes da classe Aluno.
"""
import unittest

from aluno import Aluno


class TestAluno(unittest.TestCase):
    """Testa a classe Aluno."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.aluno = Aluno(nome="João Silva", matricula="2023001")

    def test_inicializacao(self):
        """Verifica se o aluno é inicializado corretamente."""
        self.assertEqual(self.aluno.nome, "João Silva")
        self.assertEqual(self.aluno.matricula, "2023001")
        self.assertEqual(self.aluno.notas, {})
        self.assertEqual(self.aluno.faltas, {})

    def test_adicionar_nota(self):
        """Verifica se a nota é adicionada corretamente."""
        self.aluno.adicionar_nota("Matemática", 8.5)
        self.assertEqual(self.aluno.notas["Matemática"], [8.5])
        
        self.aluno.adicionar_nota("Matemática", 7.0)
        self.assertEqual(self.aluno.notas["Matemática"], [8.5, 7.0])

    def test_calcular_media(self):
        """Verifica se a média é calculada corretamente."""
        self.aluno.adicionar_nota("Matemática", 8.0)
        self.aluno.adicionar_nota("Matemática", 7.0)
        self.aluno.adicionar_nota("Matemática", 9.0)
        
        media = self.aluno.calcular_media("Matemática")
        self.assertAlmostEqual(media, 8.0)

    def test_verificar_aprovacao(self):
        """Verifica se a aprovação é calculada corretamente."""
        # Teste com média suficiente
        self.aluno.adicionar_nota("Matemática", 7.0)
        self.aluno.adicionar_nota("Matemática", 7.0)
        self.assertTrue(self.aluno.verificar_aprovacao("Matemática"))
        
        # Teste com média insuficiente
        self.aluno.adicionar_nota("Português", 5.0)
        self.aluno.adicionar_nota("Português", 5.0)
        self.assertFalse(self.aluno.verificar_aprovacao("Português"))

    def test_registrar_falta(self):
        """Verifica se as faltas são registradas corretamente."""
        self.aluno.registrar_falta("Matemática")
        self.assertEqual(self.aluno.faltas["Matemática"], 1)
        
        self.aluno.registrar_falta("Matemática")
        self.assertEqual(self.aluno.faltas["Matemática"], 2)

    def test_calcular_frequencia(self):
        """Verifica se a frequência é calculada corretamente."""
        total_aulas = 20
        self.aluno.registrar_falta("Matemática")
        self.aluno.registrar_falta("Matemática")
        
        frequencia = self.aluno.calcular_frequencia("Matemática", total_aulas)
        self.assertAlmostEqual(frequencia, 90.0)  # 18/20 = 90%


if __name__ == "__main__":
    unittest.main() 