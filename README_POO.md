# Sistema Bancário com Programação Orientada a Objetos (POO)

## Visão Geral

Este projeto apresenta uma refatoração do sistema bancário original (`sistema.py`) para uma versão orientada a objetos (`sistema_poo.py`), demonstrando os benefícios e boas práticas da POO.

## Estrutura das Classes

### 1. Classe `Usuario`
**Responsabilidades:**
- Representar um usuário do sistema bancário
- Gerenciar dados pessoais (nome, CPF, data de nascimento, endereço)
- Validação e limpeza de CPF

**Atributos:**
- `nome`: Nome completo do usuário
- `data_nascimento`: Data de nascimento
- `cpf`: CPF limpo (apenas números)
- `endereco`: Endereço completo

**Métodos:**
- `_limpar_cpf()`: Método estático para remover caracteres não numéricos do CPF
- `__str__()`: Representação em string do usuário

### 2. Classe `Conta`
**Responsabilidades:**
- Representar uma conta bancária
- Gerenciar operações financeiras (depósito, saque)
- Controlar limites e regras de negócio
- Manter extrato de transações

**Atributos:**
- `agencia`: Número da agência
- `numero_conta`: Número da conta
- `usuario`: Referência ao usuário titular
- `saldo`: Saldo atual da conta
- `limite`: Limite de saque
- `extrato`: Histórico de transações
- `numero_saques`: Contador de saques realizados
- `limite_saques`: Limite máximo de saques

**Métodos:**
- `depositar()`: Realiza depósito na conta
- `sacar()`: Realiza saque da conta (com validações)
- `exibir_extrato()`: Mostra o extrato da conta
- `__str__()`: Representação em string da conta

### 3. Classe `Banco`
**Responsabilidades:**
- Gerenciar usuários e contas
- Coordenar operações bancárias
- Implementar regras de negócio do banco

**Atributos:**
- `nome`: Nome do banco
- `agencia`: Número da agência
- `usuarios`: Lista de usuários cadastrados
- `contas`: Lista de contas bancárias

**Métodos:**
- `cadastrar_usuario()`: Cadastra novo usuário
- `cadastrar_conta_bancaria()`: Cria nova conta
- `buscar_usuario_por_cpf()`: Localiza usuário pelo CPF
- `buscar_conta_por_numero()`: Localiza conta pelo número
- `listar_contas()`: Exibe todas as contas
- `realizar_deposito()`: Coordena operação de depósito
- `realizar_saque()`: Coordena operação de saque
- `exibir_extrato_conta()`: Coordena exibição de extrato

### 4. Classe `SistemaBancario`
**Responsabilidades:**
- Interface principal do sistema
- Gerenciar o fluxo de execução
- Apresentar menu e opções ao usuário

**Atributos:**
- `banco`: Instância do banco

**Métodos:**
- `exibir_menu()`: Mostra o menu de opções
- `executar()`: Loop principal do sistema

## Benefícios da Refatoração para POO

### 1. **Encapsulamento**
- Dados e comportamentos relacionados estão agrupados em classes
- Métodos privados (como `_limpar_cpf`) protegem implementações internas
- Interface clara e bem definida para cada classe

### 2. **Reutilização de Código**
- Classes podem ser reutilizadas em outros contextos
- Métodos comuns (como busca por CPF) são centralizados
- Herança pode ser facilmente implementada para novos tipos de conta

### 3. **Manutenibilidade**
- Mudanças em uma classe não afetam outras
- Código mais organizado e fácil de entender
- Responsabilidades bem definidas

### 4. **Extensibilidade**
- Fácil adicionar novos tipos de conta (ContaCorrente, ContaPoupanca)
- Novos tipos de usuário podem herdar da classe base
- Novas funcionalidades podem ser adicionadas sem modificar código existente

### 5. **Testabilidade**
- Cada classe pode ser testada independentemente
- Métodos isolados facilitam testes unitários
- Mock objects podem ser facilmente criados

## Melhorias Implementadas

### 1. **Type Hints**
- Uso de `typing` para melhor documentação
- `List[Usuario]`, `Optional[Conta]` para clareza de tipos

### 2. **Documentação**
- Docstrings em todos os métodos
- Comentários explicativos em métodos complexos

### 3. **Validação de Retorno**
- Métodos retornam `bool` para indicar sucesso/falha
- Melhor tratamento de erros

### 4. **Métodos Mágicos**
- `__str__()` para representação em string
- Facilita debugging e logging

### 5. **Separação de Responsabilidades**
- Cada classe tem uma responsabilidade específica
- Reduz acoplamento entre componentes

## Como Executar

```bash
python sistema_poo.py
```

## Comparação com a Versão Original

| Aspecto | Versão Original | Versão POO |
|---------|----------------|------------|
| Estrutura | Funções soltas | Classes organizadas |
| Dados | Dicionários | Atributos de classe |
| Reutilização | Baixa | Alta |
| Manutenibilidade | Média | Alta |
| Extensibilidade | Baixa | Alta |
| Testabilidade | Difícil | Fácil |

## Próximos Passos Sugeridos

1. **Implementar herança** para diferentes tipos de conta
2. **Adicionar persistência** de dados (arquivo/banco de dados)
3. **Implementar validações** mais robustas
4. **Adicionar logs** para auditoria
5. **Criar testes unitários** para cada classe
6. **Implementar interface gráfica** usando as classes existentes 