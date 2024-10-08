from datetime import datetime
from src.domain.entities.usuario import Usuario
from src.domain.entities.conta import Conta

class OperacoesAdmin():
    def __init__(self):
        self.payload = {}
    
    def _validar_usuario(self, lista_usuarios, novo_usuario):
        for usuario in lista_usuarios:
            if usuario.cpf == novo_usuario.cpf:
                return False
        return True
    
    def cadastrar_usuario(self, nome:str, data_nascimento: datetime, cpf: str, logadouro: dict) -> Usuario:
        self.payload.update({"nome":nome})
        self.payload.update({"data_nascimento":data_nascimento})
        self.payload.update({"cpf":cpf})
        self.payload.update({"logadouro": logadouro})
        return Usuario(**self.payload)

    def cadastrar_conta(self, usuario: Usuario, numero: str):
        return Conta(numero, usuario)




