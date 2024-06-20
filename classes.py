from abc import ABC, abstractmethod

class Conta:
    def __init__(self, cliente, numero, saldo=0, agencia=None, historico=None):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico
    
    def saldo(self) -> float:
        pass
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        pass

    def sacar(self, valor) -> bool:
        pass

    def depositar(self, valor) -> bool:
        pass


class Cliente:
    def __init__(self, endereco, contas):
            self._endereco = endereco
            self._contas = contas
    
    def realizar_transacao(self, conta, transacao):
        pass
    
    def adicionar_conta(self, conta):
        pass


class Transacao(ABC):
    @abstractmethod
    def regitrar(conta):
        pass
         
class Deposito:
    def __init__(self, valor) -> float:
        self._valor = valor

class Saque:
    def __init__(self, valor) -> float:
        self._valor = valor

class Historico:
    def adicionar_transacao(transacao):
        pass

class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class ContaCorrente:
    def __init__(self, limite, limite_saques):
        self._limite = limite
        self._limite_saques = limite_saques
