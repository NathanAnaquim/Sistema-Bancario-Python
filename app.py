menu = """

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

while True: 
    opcao = input (menu)

    if opcao == "1" : 
        print ("Depósito") 

        valor_depositado = float(input("Insira o valor que deseja depositar: "))
        if valor_depositado > 0 :
            saldo += valor_depositado
            extrato += f"Depósito: {valor_depositado:.2f}\n"
            print("Valor depositado com sucesso")
                        
        else : 
            print("Digite um valor válido para depósito!!")
           

    elif opcao == "2":
        print ("Saque")

        valor_sacado = float(input("Insira o valor que deseja sacar: "))

        excedeu_saldo  = valor_sacado > saldo 
    
        excedeu_limite = valor_sacado > limite 

        excedeu_saque = numero_saques >= LIMITE_SAQUES 

        if excedeu_saldo: 
            print("Erro, você não tem saldo o suficiente")

        elif excedeu_limite:
            print("Erro, o valor do saque excedeu o limite")

        elif excedeu_saque:
            print("Erro, você atingiu numero máximo de saque diário")

        elif valor_sacado > 0 :
            saldo  -= valor_sacado
            numero_saques += 1
            extrato += f"Saque: {valor_sacado:.2f}\n"
            print("Valor sacado com sucesso ")
                        
        else :
            print("Você não pode sacar esse valor ou ja excedeu o limite diário de saques ")
   
        
    elif opcao == "3":
        print ("Extrato")
        print(f"Não teve movimentação" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        


    elif opcao == "4":
        break

    else :
        print("Opção inválida, selecione a operação desejada")









