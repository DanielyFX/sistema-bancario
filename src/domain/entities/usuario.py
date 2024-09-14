from datetime import datetime

class Usuario():
    def __init__(self, nome: str, data_nascimento: datetime, cpf: str, logadouro: dict):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._logadouro = logadouro

    @property
    def nome(self) -> str:
        """getter para o nome do titular da conta"""
        return self._nome
    
    @property
    def data_nascimento(self) -> str:
        return self._data_nascimento
    
    @property
    def cpf(self) -> str:
        return self._cpf
    
    @property
    def logadouro(self) -> str:
        return self._logadouro
    
    @logadouro.setter
    def logadouro(self, novo_logadouro: str):
        self.logadouro = novo_logadouro

    