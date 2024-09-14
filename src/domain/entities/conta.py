from src.domain.entities.usuario import Usuario

class Conta(Usuario):
    def __init__(self, numero, usuario: Usuario):
        super().__init__(usuario.nome, usuario.data_nascimento, usuario.cpf, usuario.logadouro)
        self._numero = numero
        self._limite = 1000
        self._saldo = 0
        self._LIMITE_SAQUES = 3
        self._LIMITE_OPERACOES = 10
        self._extrato = "--------------EXTRATO------------\n"

    @property
    def numero(self):
        """getter para o número da conta"""
        return self._numero
    
    @property
    def limite(self):
        """getter para o limite da conta"""
        return self._limite
    
    @limite.setter
    def limite(self, valor):
        """função para modificar o limite da conta"""
        if valor < 0:
            raise ValueError("O limite da conta não pode ser negativo!")
        else:
            self._limite = valor
    
    @property
    def saldo(self):
        """getter para o saldo da conta"""
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        """setter para modificar valor do saldo"""
        if valor < 0:
            raise ValueError("O valor do saldo não pode ser menor do que zero!")
        else:
            self._saldo = valor
    
    @property
    def LIMITE_SAQUES(self):
        """getter para limite de saques"""
        return self._LIMITE_SAQUES
    
    @LIMITE_SAQUES.setter
    def LIMITE_SAQUES(self, valor):
        """setter para limite de saques"""
        if valor < 0:
            raise ValueError("O número de saques não pode ser menor do que zero")
        else:
            self._LIMITE_SAQUES = valor
    
    @property
    def LIMITE_OPERACOES(self):
        """getter para limite de saques"""
        return self._LIMITE_OPERACOES
    
    @LIMITE_OPERACOES.setter
    def LIMITE_OPERACOES(self, valor):
        """setter para limite de saques"""
        if valor < 0:
            raise ValueError("O número de saques não pode ser menor do que zero")
        else:
            self._LIMITE_OPERACOES = valor
        
    @property
    def extrato(self):
        """getter para extrato da conta"""
        return self._extrato
    
    @extrato.setter
    def extrato(self, valor):
        """setter para modificar o extrato da conta"""
        if valor == "":
            raise ValueError("O extrato não pode ser vazio! Ele já está vazio!!!")
        else:
            self._extrato = valor



