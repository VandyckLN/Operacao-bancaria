from datetime import datetime, timezone, timedelta
from collections import defaultdict

# Lista para armazenar o extrato
extrato = []
# Dicionário para contar transações por dia
transacoes_diarias = defaultdict(int)

# Estruturas para armazenamento
usuarios = {}  # Dicionário para armazenar usuários
contas = {}  # Dicionário para armazenar contas
ultimo_numero_conta = 0  # Contador para gerar números de conta
AGENCIA = "0001"  # Agência fixa
NOME_BANCO = "VdkBANK"


def obter_hora_sp():
    fuso_sp = timezone(timedelta(hours=-3))
    data_sp = datetime.now(fuso_sp)
    return data_sp.strftime("%d/%m/%Y %H:%M:%S")


def obter_data_atual():
    fuso_sp = timezone(timedelta(hours=-3))
    data_sp = datetime.now(fuso_sp)
    return data_sp.strftime("%d/%m/%Y")


def registrar_transacao(tipo, valor, saldo):
    data_hora = obter_hora_sp()
    data = obter_data_atual()

    # Incrementa o contador de transações do dia
    transacoes_diarias[data] += 1

    # Registra a transação no extrato
    extrato.append(
        {"tipo": tipo, "valor": valor, "saldo": saldo, "data_hora": data_hora}
    )


def mostrar_extrato():
    print("\n=============== EXTRATO ===============")
    for operacao in extrato:
        print(f"Data/Hora: {operacao['data_hora']}")
        print(f"Tipo: {operacao['tipo']}")
        print(f"Valor: R$ {operacao['valor']:.2f}")
        print(f"Saldo: R$ {operacao['saldo']:.2f}")
        print("=====================================")


data = datetime.now(timezone.utc)
print(data)

# Definindo as variáveis iniciais da conta
conta = "bradesco"
saldo = 830.00  # Corrigido: usar ponto ao invés de vírgula para decimais
limite_diario = 1000  # Corrigido: usar underscore para nomes compostos


def gerar_numero_conta():
    global ultimo_numero_conta
    ultimo_numero_conta += 1
    return str(ultimo_numero_conta).zfill(11)  # Preenche com zeros à esquerda


def validar_cpf(cpf):
    """
    Valida o CPF considerando as seguintes regras:
    - Deve ter exatamente 11 dígitos
    - Todos os caracteres devem ser números
    - Não pode ser uma sequência de números iguais
    """
    # Remove caracteres não numéricos
    cpf = "".join(filter(str.isdigit, cpf))

    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se não é uma sequência de números iguais
    if len(set(cpf)) == 1:
        return False

    # Verifica se todos são dígitos
    if not cpf.isdigit():
        return False

    return True


def criar_usuario():
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF (apenas números): ")

    # Validação do CPF
    if not validar_cpf(cpf):
        print("CPF inválido! O CPF deve conter exatamente 11 números.")
        return None

    if cpf in usuarios:
        print("CPF já cadastrado!")
        return None

    usuario = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": input("Digite sua data de nascimento: "),
        "email": input("Digite seu email: "),
        "telefone": input("Digite seu telefone: "),
        "endereco": input("Digite seu endereço: "),
        "contas": [],
    }
    usuarios[cpf] = usuario
    print(f"\nUsuário {nome} criado com sucesso!")
    print(f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
    return cpf


def criar_conta(cpf):
    if cpf not in usuarios:
        print("Usuário não encontrado. Crie um usuário primeiro.")
        return

    numero_conta = gerar_numero_conta()
    conta = {"agencia": AGENCIA, "numero": numero_conta, "saldo": 0.0, "titular": cpf}
    contas[numero_conta] = conta
    usuarios[cpf]["contas"].append(numero_conta)
    print(f"\nConta criada com sucesso!")
    print(f"Agência: {AGENCIA}")
    print(f"Número da conta: {numero_conta}")
    print(f"Titular: {usuarios[cpf]['nome']}")


def selecionar_conta(cpf):
    if cpf not in usuarios or not usuarios[cpf]["contas"]:
        print("Nenhuma conta encontrada.")
        return None

    print("\nContas disponíveis:")
    for i, numero_conta in enumerate(usuarios[cpf]["contas"], 1):
        print(f"{i}. Conta: {numero_conta}")

    try:
        opcao = int(input("Selecione o número da conta: ")) - 1
        if 0 <= opcao < len(usuarios[cpf]["contas"]):
            return usuarios[cpf]["contas"][opcao]
    except ValueError:
        pass
    print("Opção inválida")
    return None


def realizar_transacao(tipo, cpf):
    numero_conta = selecionar_conta(cpf)
    if not numero_conta:
        return

    conta = contas[numero_conta]
    valor = float(input(f"Digite o valor para {tipo}: "))

    if tipo == "saque":
        if valor > conta["saldo"]:
            print("Saldo insuficiente")
            return
        conta["saldo"] -= valor
    else:  # depósito
        conta["saldo"] += valor

    print(f"\nOperação realizada com sucesso!")
    print(f"Banco: {NOME_BANCO}")
    print(f"Cliente: {usuarios[cpf]['nome']}")
    print(f"Conta: {numero_conta}")
    print(f"Novo saldo: R$ {conta['saldo']:.2f}")
    registrar_transacao(tipo, valor, conta["saldo"])


# Modificar a função operacoes_bancarias()
def operacoes_bancarias():
    cpf_atual = None

    while True:
        print(f"\n=== {NOME_BANCO} ===")
        print("1. Criar usuário")
        print("2. Criar conta")
        print("3. Selecionar usuário")
        print("4. Depositar")
        print("5. Sacar")
        print("6. Consultar saldo")
        print("7. Extrato")
        print("8. Sair")

        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                cpf_atual = criar_usuario()

            elif opcao == 2:
                if cpf_atual:
                    criar_conta(cpf_atual)
                else:
                    print("Selecione um usuário primeiro")

            elif opcao == 3:
                cpf = input("Digite o CPF do usuário: ")
                if cpf in usuarios:
                    cpf_atual = cpf
                    print(f"Usuário selecionado: {usuarios[cpf]['nome']}")
                else:
                    print("Usuário não encontrado")

            elif opcao in (4, 5):  # Depósito ou Saque
                if cpf_atual:
                    realizar_transacao("depósito" if opcao == 4 else "saque", cpf_atual)
                else:
                    print("Selecione um usuário primeiro")

            elif opcao == 6:  # Consultar saldo
                if cpf_atual:
                    numero_conta = selecionar_conta(cpf_atual)
                    if numero_conta:
                        print(f"Saldo: R$ {contas[numero_conta]['saldo']:.2f}")
                else:
                    print("Selecione um usuário primeiro")

            elif opcao == 7:
                mostrar_extrato()

            elif opcao == 8:
                print("Obrigado por utilizar nossos serviços!")
                break

            else:
                print("Opção inválida")

        except ValueError:
            print("Entrada inválida. Digite um número.")


if __name__ == "__main__":
    operacoes_bancarias()
