from src.domain.entities.conta import Conta
from src.domain.repository.conta import sacar, depoisitar, extrato, menu
import random


numero_conta = int(random.random() * 1000)
nome = "Maria"

conta = Conta(numero_conta, nome)

while True:
    print(menu())

    opt = input("Escolha uma das operações: \n")

    match (opt):
        case "d":
            valor = float(input("Insira um valor para depositar\n"))
            if isinstance(depoisitar(conta.saldo,valor), float):
                conta.saldo = depoisitar(conta.saldo, valor)
                conta.extrato = extrato(f"Saldo: {conta.saldo}", conta.extrato, f"Deposito: {valor}\n")
            else:
                print("Operação inválida!\n")

        case "s":
            valor = float(input("Insira um valor para sacar\n"))
            if isinstance(sacar(conta.saldo, valor), float):
                conta.saldo = sacar(conta.saldo, valor)
                conta.limite = conta.limite - 1
                conta.extrato = extrato(f"Saldo: {conta.saldo}", conta.extrato, f"Saque: {valor}\n")
            else:
                print("Operação inválida!!!\n")
        case "e":
            print(conta.extrato)
        case "q":
            print("Tenha um ótimo dia!")
            break
        case _:
            print("Escolha uma das opções do menu!\n")