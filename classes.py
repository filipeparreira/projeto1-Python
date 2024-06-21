from abc import ABC, abstractmethod

class Conta:
    def __init__(self, cliente, numero, saldo=0, agencia=None):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()
    
    def saldo(self) -> float:
        return self._saldo
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return ContaCorrente(cliente, numero)

    def sacar(self, valor) -> bool:
        pass

    def depositar(self, valor) -> bool:
        pass


class Cliente:
    def __init__(self, endereco, contas):
            self._endereco = endereco
            self._contas = list(contas)
    
    def realizar_transacao(self, conta, transacao):
        self._contas.index(conta)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)


class Transacao(ABC):
    @abstractmethod
    def regitrar(conta):
        pass
         
class Deposito(Transacao):
    def __init__(self, valor) -> float:
        self._valor = valor
    
    def registrar(self, conta):
        if (conta.depositar(self._valor)):
            return self.__str__
        else:
            print("Não foi possível realizar a transação")

    def __str__(self) -> str:
        return '|' + f"Deposito: R$ {self._valor:.2f}".center(40) + '|'
            

class Saque(Transacao):
    def __init__(self, valor) -> float:
        self._valor = valor

    def registrar(self, conta):
        if (conta.sacar(self._valor)):
            return self.__str__
        else:
            print("Não foi possível realizar a transação")
    
    def __str__(self) -> str:
        return '|' + f"Saque: R$ {self._valor:.2f}".center(40) + '|'

class Historico:
    def __init__(self, historico = list()):
        self._historico = historico
        
    def adicionar_transacao(self, transacao):
        self._historico.append(transacao)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        self._limite = limite
        self._limite_saques = limite_saques
        super()._cliente = cliente
        super()._numero = numero

    def sacar(self, valor):
        if (valor - super()._saldo > 0 and self._limite_saques > 0 and valor <= 500):
            super()._saldo -= valor
            limite_saque -= 1
            return True
        else:
            return False
    
    def depositar(self, valor):
        if (valor > 0):
            super()._saldo += valor
            return True
        else:
            return False


