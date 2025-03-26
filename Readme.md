# Sistema Bancário em Python 🏦

## 📋 Descrição

Sistema bancário desenvolvido em Python que simula operações bancárias completas, incluindo cadastro de usuários, múltiplas contas e controle de transações.

## 🔧 Funcionalidades

### Usuários
- Cadastro completo de usuários
- Validação de CPF (11 dígitos)
- Armazenamento de dados pessoais
- Múltiplas contas por usuário

### Contas
- Geração automática de número de conta (11 dígitos)
- Agência fixa (0001)
- Vinculação com usuário
- Múltiplas contas por cliente

### Operações
- Saque com limite diário de R$ 1.000,00
- Depósito com confirmação
- Consulta de saldo
- Extrato detalhado com data e hora
- Limite de 10 transações diárias
- Registro de todas as operações

## 🏛️ Dados Bancários
- Nome do Banco: VdkBANK
- Agência: 0001
- Contas: 11 dígitos sequenciais

## 🚀 Como usar

1. Clone o repositório
```bash
git clone https://github.com/VandyckLN/Operacao-bancaria.git
```

2. Execute o programa
```bash
python Operacao-bancarias.py
```

## 💻 Tecnologias Utilizadas
- Python 3.x
- Módulos: 
  - datetime (controle de data/hora)
  - collections (gestão de transações)

## 🔒 Validações de Segurança
- Validação completa de CPF
- Verificação de saldo antes das operações
- Confirmação de operações de depósito
- Controle de limite diário para saques
- Limite de transações diárias
- Proteção contra valores negativos

## 📊 Controles
- Extrato com data e hora das operações
- Contador de transações diárias
- Múltiplas contas por usuário
- Saldo individual por conta

## 👨‍💻 Autor
[Vandyck LN](https://github.com/VandyckLN)

## 📜 Licença
Este projeto está sob a licença MIT.
