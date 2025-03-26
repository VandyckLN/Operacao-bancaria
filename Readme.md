# Sistema de Operações Bancárias

## 📋 Descrição

Sistema simples de operações bancárias desenvolvido em Python que simula funcionalidades básicas de um caixa eletrônico.

## 🔧 Funcionalidades

### 1. Saque

- Permite realizar saques da conta
- Verifica limite diário de R$ 1.000,00
- Verifica se há saldo suficiente
- Exibe o saldo atualizado após a operação
- Apresenta mensagens de erro em caso de:
  - Saldo insuficiente
  - Limite diário excedido

### 2. Depósito

- Permite realizar depósitos na conta
- Solicita confirmação da operação
- Valida valores negativos
- Atualiza o saldo automaticamente
- Exibe o saldo atualizado após a operação

### 3. Consulta de Saldo

- Exibe o saldo atual da conta
- Formata o valor com duas casas decimais
- Apresenta o valor em reais (R$)

### 4. Sistema de Menu

- Interface intuitiva por linha de comando
- Opções numeradas de 4 a 7
- Opção de saída do sistema
- Validação de opções inválidas

## 🚀 Como Executar

1. Certifique-se de ter Python 3.x instalado
2. Clone o repositório
3. Execute o arquivo `Operacao-bancarias.py`

```bash
python Operacao-bancarias.py
```

## 💰 Configurações Iniciais

- Saldo inicial: R$ 830,00
- Limite diário para saques: R$ 1.000,00
- Banco: Bradesco

## 🔒 Validações de Segurança

- Verificação de saldo antes das operações
- Confirmação de operações de depósito
- Validação de valores negativos
- Controle de limite diário para saques

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Estruturas de controle de fluxo
- Manipulação de tipos de dados
- Formatação de strings

## 📝 Notas

- O sistema mantém o saldo em memória durante a execução
- Todas as operações são formatadas com duas casas decimais
- O sistema continua em execução até que a opção de saída seja selecionada

## 👨‍💻 Autor

[Seu Nome]

## 📜 Licença

Este projeto está sob a licença [TIPO_DE_LICENÇA].
