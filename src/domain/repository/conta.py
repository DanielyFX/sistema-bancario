from src.domain.entities.conta import Conta


class OperacoesConta():
    def sacar(self, saque_limite, op_limite, saldo, valor):
        if saque_limite != 0 and op_limite != 0:
            if saldo >= valor:
                return saldo-valor
            else:
                return "Operação inválida!\n"
        else:
           return "limite de saques atingido! tente novamente outro dia!\n"

    def depoisitar(self, op_limite, saldo, valor):
        if op_limite != 0:
            if valor > 0:
                return saldo+valor
            else:
                return "Depósitos não podem ser negativos!!\n"
        else:
            return "limite de operações atingido! tente novamente outro dia!\n"

    def extrato(self, saldo, extrato, operacao, data):
        return f"\
        {extrato} {saldo} \n {operacao}\n {data}\n \
------------------------------------------\n"

    