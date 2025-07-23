menu1 = """

[1] Criar Usuário
[2] Criar Conta Corrente

"""

menu2 = """

[1] Depositar 
[2] Sacar
[3] Extrato 
[4] Sair

"""

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor_depositado = 0
valor_sacado = 0

usuarios = ()

def criar_usuario( nome, data_de_nascimento, cpf, endereco): 
    nome = input("Digite seu nome")
    data_de_nascimento = input("Digite sua data de nascimento")
    cpf = (input("Digite seu CPF"))
    while True:
        cpf = input("Digite seu CPF: ")
        
        cpf_ja_cadastrado = any(usuario["CPF"] == cpf for usuario in usuarios)
        
        if cpf_ja_cadastrado:
            print("Erro, esse CPF ja esta Cadastrado")
        else:
            break
    

    endereco = {
        "rua": input("Digite a sua rua:"),
        "numero": input("Digite o numero da casa:"),
        "bairro": input("Digite o seu bairro:"),
        "cidade": input("Digite a sua cidade:"),
        "sigla_estado": input("Digite a sigla do seu estado:")
        }
    
    return nome, data_de_nascimento, cpf, endereco  



def criar_conta_corrente():
    print()


def deposito(saldo, extrato):
    valor_depositado = float(input("Insira o valor que deseja depositar: "))
    if valor_depositado > 0 :
        saldo += valor_depositado
        extrato += f"Depósito: {valor_depositado:.2f}\n"
        print("Valor depositado com sucesso")      
        return saldo, extrato
    else : 
        print("Digite um valor válido para depósito!!")
        return saldo , extrato

def sacar(* ,saldo ,extrato ,numero_saques):
    valor_sacado = float(input("Insira o valor que deseja sacar: "))

    excedeu_saldo  = valor_sacado > saldo 
    
    excedeu_limite = valor_sacado > limite 

    excedeu_saque = numero_saques >= LIMITE_SAQUES 

    if excedeu_saldo: 
            print("Erro, você não tem saldo o suficiente")
            return saldo, extrato, numero_saques 

    elif excedeu_limite:
            print("Erro, o valor do saque excedeu o limite")
            return saldo, extrato, numero_saques

    elif excedeu_saque:
            print("Erro, você atingiu numero máximo de saque diário")
            return saldo, extrato, numero_saques

    elif valor_sacado > 0 :
            saldo  -= valor_sacado
            numero_saques += 1
            extrato += f"Saque: {valor_sacado:.2f}\n"
            print("Valor sacado com sucesso ")            
            return saldo, extrato, numero_saques 
    else :
            print("Você não pode sacar esse valor ou ja excedeu o limite diário de saques ")
            return saldo, extrato, numero_saques

def visualizar_extrato(saldo , /, extrato):
    print(f"Não teve movimentação" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    return saldo, extrato



while True: 
    opcao = input(menu1)
    if opcao == "1": 
        nome, data_de_nascimento, cpf, endereco = criar_usuario( nome, data_de_nascimento, cpf, endereco)

    elif opcao == "2" :


        if opcao == "1" : 
            saldo, extrato = deposito(saldo, extrato)
        
        elif opcao == "2":
            saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, numero_saques=numero_saques)

        elif opcao == "3":
            saldo, extrato = visualizar_extrato(saldo, extrato = extrato)
            
        elif opcao == "4":
            break
        else :
            print("Opção inválida, selecione a operação desejada") 









