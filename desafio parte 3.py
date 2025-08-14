from abc import ABC, abstractmethod


class Cliente: 
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente): 
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta: 
    def __init__(self, numero, cliente):
        self._saldo = 0 
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod 
    def nova_conta(cls, cliente, numero): 
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self): 
        return self._numero
    
    @property 
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico 
    
    def sacar(self, valor): 
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo: 
            print("Saldo insuficiente")

        elif valor > 0: 
            self._saldo -= valor
            print("Saque feito")
            return True
    
        else: 
            print("Valor inválido")

        return False
    

    def depositar(self, valor): 
        if valor > 0: 
            self._saldo += valor
            print("Depósito realizado")
        else: 
            print("Valor inválido")
            return False
        
        return True


class ContaCorrente(Conta): 
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite 
        self.limite_saques = limite_saques

    def sacar(self, valor): 
        numero_saques = len(
            [t for t in self.historico.transacoes if t["tipo"] == Saque.__name__])
        
        excedeu_limite = valor > self.limite
        excedeu_saque = numero_saques >= self.limite_saques

        if excedeu_limite: 
            print("O valor do saque excedeu o limite")

        elif excedeu_saque: 
            print("Número máximo de saques excedido")

        else: 
            return super().sacar(valor)
        
        return False
    

    def __str__(self):
        return f"""
            Agência: {self.agencia}
            Conta Corrente: {self.numero}
            Titular: {self.cliente.nome}
        """


class Historico: 
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor
        })


class Transacao(ABC): 
    @property
    @abstractmethod 
    def valor(self): 
        pass 

    @abstractmethod 
    def registrar(self, conta):
        pass


class Saque(Transacao): 
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self): 
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao: 
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self): 
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao: 
            conta.historico.adicionar_transacao(self)


# Exemplo de execução
if __name__ == "__main__":
    cliente1 = PessoaFisica("Nathan", "17/05/2005", "12345678900", "Rua A")
    conta1 = ContaCorrente.nova_conta(cliente1, 1)
    cliente1.adicionar_conta(conta1)

    # Depósito
    cliente1.realizar_transacao(conta1, Deposito(1000))
    # Saque
    cliente1.realizar_transacao(conta1, Saque(200))

    print(f"Saldo final: {conta1.saldo}")
    print("Histórico:", conta1.historico.transacoes)
