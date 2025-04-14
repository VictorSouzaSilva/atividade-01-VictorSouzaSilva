# Exercícios de TDD - Prática de Desenvolvimento Guiado por Testes

Este repositório contém exercícios práticos de TDD (Test-Driven Development) que abordam diferentes cenários do mundo real. O primeiro exercício será desenvolvido em conjunto, servindo como exemplo, e os demais serão implementados pelos alunos.

## Exercícios Disponíveis

### 1. Sistema de Pagamento de Funcionários (Desenvolvido em Conjunto)
Este exercício será desenvolvido em conjunto como exemplo prático de TDD. Vamos implementar um sistema de cálculo de pagamento de funcionários considerando:

**Aspectos a serem testados:**
- Cálculo correto do salário base
- Adição do custo do empregador
- Cálculo de comissão
- Validação de valores negativos
- Tratamento de horas extras
- Cálculo de benefícios

**Arquivos:**
- `funcionario/funcionario.py`
- `funcionario/test_funcionario.py`

### 2. Sistema de Controle de Estoque (Exercício para Alunos)
Implemente um sistema de controle de estoque com os seguintes requisitos:

**Aspectos a serem testados:**
- Controle de quantidade (mínimo e máximo)
- Cálculo de valor total do estoque
- Controle de validade dos produtos
- Registro de movimentações
- Alertas de estoque baixo
- Cálculo de perdas

**Requisitos de Cobertura:**
- Mínimo de 90% de cobertura de código
- Testes para todos os métodos públicos
- Testes para casos de erro e exceções
- Testes para valores limite

**Arquivos:**
- `estoque/produto.py`
- `estoque/test_produto.py`

## Como Usar

### Para o Exercício de Funcionários (Desenvolvido em Conjunto)
1. Clone este repositório
2. Instale as dependências:
   ```bash
   pip install pytest pytest-cov
   ```
3. Navegue até a pasta `funcionario`
4. Execute os testes:
   ```bash
   pytest
   ```
5. Siga o desenvolvimento guiado pelo professor

### Para o Exercício de Estoque (Implementação Individual)
1. Clone este repositório
2. Instale as dependências:
   ```bash
   pip install pytest pytest-cov
   ```
3. Navegue até a pasta `estoque`
4. Implemente os testes e o código seguindo o ciclo TDD
5. Verifique a cobertura dos testes:
   ```bash
   pytest --cov=./ --cov-report=term-missing
   ```

## Critérios de Avaliação

O GitHub Actions irá analisar para cada exercício:
- Porcentagem de cobertura de código (mínimo 90%)
- Número de testes passados/falhados
- Porcentagem de testes passados
- Qualidade dos testes (completude e robustez)

## Metodologia TDD

Para cada exercício, siga o ciclo TDD:

1. **Red**: Escreva um teste que falha
2. **Green**: Faça o teste passar com o mínimo de código possível
3. **Refactor**: Melhore o código mantendo os testes passando

## Dicas para Implementação

1. Comece pelos casos mais simples
2. Mantenha os testes passando após cada mudança
3. Refatore o código quando necessário
4. Verifique a cobertura dos testes após cada implementação
5. Documente seu código com docstrings claras
6. Use type hints para melhor legibilidade
7. Pense em casos de borda e exceções
8. Mantenha os testes independentes entre si

## Entrega e Avaliação

1. Faça um fork deste repositório
2. Implemente o exercício de estoque
3. Certifique-se de que todos os testes passam
4. Verifique se a cobertura está acima de 90%
5. Faça um pull request com sua implementação
6. O professor avaliará:
   - Qualidade dos testes
   - Cobertura de código
   - Organização do código
   - Documentação
   - Seguimento do ciclo TDD

## Avaliação de Cobertura com GitHub Actions

O GitHub Actions está configurado para avaliar automaticamente a cobertura de testes de cada exercício. Aqui está como funciona:

### Processo de Avaliação

1. **Execução Automática**
   - Os testes são executados automaticamente a cada push
   - A cobertura é calculada para cada arquivo Python
   - Um relatório detalhado é gerado

2. **Métricas Analisadas**
   - **Cobertura Total**: Porcentagem de linhas de código cobertas por testes
   - **Cobertura por Arquivo**: Detalhamento da cobertura em cada arquivo
   - **Linhas Não Cobertas**: Identificação específica das linhas sem testes

3. **Visualização dos Resultados**
   - Os resultados são exibidos na aba "Actions" do GitHub
   - Um badge de cobertura é atualizado no README
   - Relatório detalhado disponível no artefato "test-report"

### Critérios de Aprovação

Para ser aprovado, seu código deve:
- Ter no mínimo 90% de cobertura total
- Ter todos os métodos públicos testados
- Ter testes para casos de erro e exceções
- Ter testes para valores limite

### Como Verificar Localmente

Antes de fazer push, você pode verificar a cobertura localmente:
```bash
# Ver cobertura geral
pytest --cov=./ --cov-report=term-missing

# Ver cobertura detalhada por arquivo
pytest --cov=./ --cov-report=html
```

### O que Fazer se a Cobertura Estiver Baixa

1. Verifique o relatório para identificar as linhas não cobertas
2. Adicione testes para os casos não cobertos
3. Execute os testes localmente para confirmar a melhoria
4. Faça push das alterações para atualizar a cobertura

### Exemplo de Badge de Cobertura

![Cobertura de Testes](https://img.shields.io/badge/coverage-90%25-green) 