menu1 = """

[1] Criar Usuário
[2] Criar Conta Corrente
[3] Acessar Conta
[4] Sair

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
AGENCIA = "0001"
numero_da_conta = 1

usuarios = []
contas = []

def criar_usuario(): 
    nome = input("Digite seu nome: ")
    data_de_nascimento = input("Digite sua data de nascimento: ")

    while True:
        cpf = input("Digite seu CPF: ")
        
        if any(usuario["cpf"] == cpf for usuario in usuarios):
            print("Erro, esse CPF ja esta Cadastrado")

        else:
            break
    
    endereco = {
        "rua": input("Digite a sua rua: "),
        "numero": input("Digite o numero da casa: "),
        "bairro": input("Digite o seu bairro: "),
        "cidade": input("Digite a sua cidade: "),
        "sigla_estado": input("Digite a sigla do seu estado: ")
        }
    
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_de_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuario criado")
    return cpf


def criar_conta_corrente():
    global numero_da_conta
    cpf = input("Digite o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    
    if usuario:
        conta = {
            "agencia": AGENCIA,
            "numero_conta": numero_da_conta,
            "usuario": usuario
        }
        contas.append(conta)
        print(f"Conta criada com sucesso! Número: {numero_da_conta} Agencia {AGENCIA}")
        numero_da_conta += 1
        return conta
    else:
        print("Usuário não encontrado. Crie um usuário primeiro.")
        return None



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

def acessar_conta():
    cpf = input("Digite seu CPF: ")
    conta = next((c for c in contas if c["usuario"]["cpf"] == cpf), None)
    
    if conta:
        print(f"\nBem-vindo, {conta['usuario']['nome']}!")
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']}")
        return True, conta
    else:
        print("Conta não encontrada.")
        return False, None

while True: 
    opcao = input(menu1)
    if opcao == "1": 
        criar_usuario()

    elif opcao == "2" :
        criar_conta_corrente()

    elif opcao == "3":
        acesso, conta = acessar_conta()
        if acesso:
            saldo_conta = 0
            extrato_conta = ""
            saques_conta = 0

        while True: 
        
         opcao = input(menu2)
         if opcao == "1" : 
            saldo_conta, extrato_conta = deposito(saldo_conta, extrato_conta)

        
         elif opcao == "2":
             saldo_conta, extrato_conta, saques_conta = sacar(
                        saldo=saldo_conta,
                        extrato=extrato_conta,
                        numero_saques=saques_conta
                    )

         elif opcao == "3":
            visualizar_extrato(saldo_conta, extrato=extrato_conta)
         elif opcao == "4":
            break
         else :
            print("Opção inválida, selecione a operação desejada") 
            
    elif opcao == "4":
     break
    else :
        print("Opção inválida, selecione a operação desejada") 









