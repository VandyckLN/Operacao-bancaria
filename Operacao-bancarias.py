from datetime import datetime, timezone, timedelta
from collections import defaultdict

# Lista para armazenar o extrato
extrato = []
# Dicionário para contar transações por dia
transacoes_diarias = defaultdict(int)


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


# Função principal do programa
def operacoes_bancarias():
    saldo_atual = saldo  # Criando uma variável local para manipular o saldo

    while True:
        data_atual = obter_data_atual()
        num_transacoes = transacoes_diarias[data_atual]

        print(f"\nData e hora atual: {obter_hora_sp()}")
        print(f"Transações realizadas hoje: {num_transacoes}/10")

        if num_transacoes >= 10:
            print("\nAVISO: Você atingiu o limite de transações diárias!")
            mostrar_extrato()
            break

        print("""
        Escolha uma opção:
        [4] Sacar
        [5] Depositar
        [6] Saldo
        [7] Sair
        [8] Extrato
        """)

        try:
            opcao = int(input("Digite a opção desejada: "))

            if opcao == 4:
                valor_saque = float(input("Digite o valor que deseja sacar: "))
                if valor_saque > limite_diario:
                    print("Limite diário excedido")
                elif valor_saque > saldo_atual:
                    print("Saldo insuficiente")
                else:
                    saldo_atual -= valor_saque
                    print("Saque realizado com sucesso")
                    print(f"Saldo atual: R$ {saldo_atual:.2f}")
                    registrar_transacao("Saque", valor_saque, saldo_atual)

            elif opcao == 5:
                valor_deposito = float(input("Digite o valor que deseja depositar: "))
                if valor_deposito < 0:
                    print("Valor inválido")
                else:
                    confirmacao = input("Confirma a operação? (sim/não): ").lower()
                    if confirmacao == "sim":
                        saldo_atual += valor_deposito
                        print("Depósito realizado com sucesso")
                        print(f"Saldo atual: R$ {saldo_atual:.2f}")
                        registrar_transacao("Depósito", valor_deposito, saldo_atual)

            elif opcao == 6:
                print(f"Saldo atual: R$ {saldo_atual:.2f}")
                registrar_transacao("Consulta Saldo", 0, saldo_atual)

            elif opcao == 7:
                print("Obrigado por utilizar nossos serviços")
                mostrar_extrato()
                break

            elif opcao == 8:
                mostrar_extrato()

            else:
                print("Opção inválida")

        except ValueError:
            print("Entrada inválida. Digite um número válido.")


if __name__ == "__main__":
    operacoes_bancarias()
