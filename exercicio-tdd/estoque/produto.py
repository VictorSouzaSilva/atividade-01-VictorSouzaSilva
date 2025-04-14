"""
Sistema de controle de estoque.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Produto:
    """Representação básica de um produto no estoque."""

    codigo: str
    nome: str
    preco: float
    quantidade: int = 0
    data_validade: Optional[datetime] = None
    estoque_minimo: int = 10

    def adicionar_estoque(self, quantidade: int) -> None:
        """Adiciona quantidade ao estoque do produto."""
        raise NotImplementedError()

    def remover_estoque(self, quantidade: int) -> bool:
        """Remove quantidade do estoque do produto."""
        raise NotImplementedError()

    def verificar_estoque_baixo(self) -> bool:
        """Verifica se o estoque está abaixo do mínimo."""
        raise NotImplementedError()

    def calcular_valor_total(self) -> float:
        """Calcula o valor total do produto em estoque."""
        raise NotImplementedError()

    def verificar_validade(self) -> bool:
        """Verifica se o produto está dentro da validade."""
        raise NotImplementedError() 