def menu():
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair\n
    """

def sacar(saldo, valor):
    if saldo >= valor:
        return saldo-valor
    else:
        return "Operação inválida!\n"

def depoisitar(saldo, valor):
    if valor > 0:
        return saldo+valor
    else:
        return "Depósitos não podem ser negativos!!\n"

def extrato(saldo, extrato, operacao):
    return f"\
    {extrato} {saldo} \n {operacao}\n \
------------------------------------------\n"

    