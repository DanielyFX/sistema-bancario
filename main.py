from src.domain.entities.conta import Conta
from src.domain.repository.conta import OperacoesConta
from src.domain.repository.admin_banco import OperacoesAdmin
from src.utils.menus import menu_user, menu_admin, menu_selecao
from datetime import datetime

op = OperacoesConta()
admin = OperacoesAdmin()

lista_contas = []
lista_users = []
numero = 1000

while True:
    print(menu_selecao())
    selecao = input("Selecione uma opção: \n")
    selecao = selecao.lower()
    match (selecao):
        case "a":
            while True:
                print(menu_admin())

                opt = input("Escolha uma das operações: \n")
                opt = opt.lower()
                
                match (opt):
                    case "c":
                        try:
                            for indice, user in enumerate(lista_users):
                                print(f"Chave:[{indice}] Usuário:{user.cpf}\n")
                            
                            usuario = int(input("Insiar a chave do usuário titular da conta: \n"))
                            conta = admin.cadastrar_conta(lista_users[usuario], numero=str(numero).strip())
                            lista_contas.append(conta)
                            numero += 1
                        except IndexError as err:
                            print(err)
                    case "u":
                        nome = input("Insira o nome do usuário \n")
                        dia = int(input("Insira o dia de nascimento do usuário: \n"))
                        mes = int(input("Insira o mês de nascimento do usuário: \n"))
                        ano = int(input("Insira o ano de nascimento do usuario: \n"))
                        cpf = input("Insira o cpf do usuário: \n")
                        rua = input("Insira a rua do usuário: \n")
                        bairro = input("Insira o bairro do usuário: \n")
                        cidade = input("Insiar a cidade do usuário: \n")
                        estado = input("Insira o estado do usuário: \n")
                        logadouro = {"rua": rua,
                                        "bairro": bairro,
                                        "cidade": cidade,
                                        "estado": estado

                                    }
                        data_nascimento = datetime(day=dia, month=mes, year=ano)

                        novo_user = admin.cadastrar_usuario(nome, data_nascimento, cpf, logadouro)
                        if admin._validar_usuario(lista_users, novo_user):
                            lista_users.append(novo_user)
                        else:
                            print("CPF de usuário já cadastrado!! \n")

                    case "e":
                        if lista_contas != []:
                            for indice, conta in enumerate(lista_contas):
                                print(f"Chave: [{indice}] Conta: {conta.numero} \n")
                        else:
                            print("Cadastre contas!!\n")
                    case "q":
                        break
                    case _:
                        print("Escolha uma das opções do menu!\n")
                    
        case "u":
            pos = None
            for conta in lista_contas:
                    print(f"Titular: {conta.nome} Numero: {conta.numero}")
            conta_numero = input("Insira o numero da sua conta: \n")
            conta_numero = conta_numero.strip()
            for conta in lista_contas:
                if conta.numero == conta_numero:
                    pos = lista_contas.index(conta)
                    break
                else:
                    print("Não existe conta com o número informado!\n")
                    break

            if pos is not None:
                conta = lista_contas[pos]

                while True:
                    print(menu_user())

                    opt = input("Escolha uma das operações: \n")
                    opt = opt.lower()

                    match (opt):
                        case "d":
                            valor = float(input("Insira um valor para depositar\n"))
                            if isinstance(op.depoisitar(conta.LIMITE_OPERACOES, conta.saldo,valor), float):
                                conta.saldo = op.depoisitar(conta.LIMITE_OPERACOES, conta.saldo, valor)
                                conta.LIMITE_OPERACOES = conta.LIMITE_OPERACOES - 1
                                conta.extrato = op.extrato(f"Saldo: {conta.saldo}", 
                                                        conta.extrato, 
                                                        f"Deposito: {valor}", 
                                                        f"DATA: {datetime.now().strftime('%d-%m-%Y %H:%M')}\n"
                                                        )
                            else:
                                print("Operação inválida!\n")

                        case "s":
                            valor = float(input("Insira um valor para sacar\n"))
                            if isinstance(op.sacar(conta.LIMITE_SAQUES, conta.LIMITE_OPERACOES, conta.saldo, valor), float):
                                conta.saldo = op.sacar(conta.LIMITE_SAQUES, conta.LIMITE_OPERACOES, conta.saldo, valor)
                                conta.LIMITE_SAQUES = conta.LIMITE_SAQUES - 1
                                conta.LIMITE_OPERACOES = conta.LIMITE_OPERACOES - 1
                                conta.extrato = op.extrato(f"Saldo: {conta.saldo}", 
                                                        conta.extrato, 
                                                        f"Saque: {valor}", 
                                                        f"DATA: {datetime.now().strftime('%d-%m-%Y %H:%M')}\n")
                            else:
                                print("Operação inválida!!!\n")
                        case "e":
                            print(conta.extrato)
                        case "q":
                            break
                        case _:
                            print("Escolha uma das opções do menu!\n")

            else:
                print("Não existe conta cadastrada com o número informado!!\n")

            
                            
        case "q":
            print("Tenha um ótimo dia!")

        case _:
            print("Escolha uma opção do menu!\n")

            