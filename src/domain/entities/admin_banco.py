from src.domain.entities.conta import Conta
import random

class AdminBanco(Conta):
    def __init__(self, nome):
        self._nome = nome
        self._matricula = random.random() * 1000
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self.nome = nome

    @property
    def matricula(self):
        return self._matricula
    
    

