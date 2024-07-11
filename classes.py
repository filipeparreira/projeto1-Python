from abc import ABC, abstractmethod

def buscar(lista, alvo):
    for i in lista:
        if i.getNumero() == alvo:
            return False
    return True

class Conta:
    def __init__(self, cliente, numero, saldo=0, agencia='001'):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()
    
    def saldo(self) -> float:
        return self._saldo
    
    def getNumero(self):
        return self._numero
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return ContaCorrente(cliente, numero)

    def sacar(self, valor) -> bool:
        if (valor - self._saldo > 0 and self._limite_saques > 0 and valor <= 500):
            self._saldo -= valor
            limite_saque -= 1
            return True
        else:
            return False

    def depositar(self, valor) -> bool:
        if (valor > 0):
            self._saldo += valor
            return True
        else:
            return False

class Cliente:
    def __init__(self, endereco, contas = list()):
            self._endereco = endereco
            self._contas = contas.copy()
    
    def realizar_transacao(self, conta, transacao):
        self._contas.index(conta)
    
    def adicionar_conta(self, conta):
        if (buscar(self._contas, conta.getNumero())):
            self._contas.append(conta)
        else:
            print("Erro: O cliente já possui essa conta.")

    def getContas(self) -> list:
        return self._contas

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
        self._historico = historico.copy()
        
    def adicionar_transacao(self, transacao):
        self._historico.append(transacao)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        super().__init__(endereco)
    
    def __str__(self) -> str:
        retorno = f'O cliente {self._nome}, possui {len(super().getContas())} contas.\n'
        if (len(super().getContas()) > 0):
            contas = ''
            for conta in super().getContas():
                contas += conta.__str__()
            retorno += contas
        return retorno

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        self._limite = limite
        self._limite_saques = limite_saques
        super().__init__(cliente, numero)

    def sacar(self, valor) -> bool:
        print("\n\nSaque:", end='')
        if (self._limite_saques > 0 and valor <= self._limite):
            if(super().sacar(valor)):
                print(" Operação concluida com sucesso!!!\n\n")
            else:
                print(" Erro na operação!!\n\n")
        else:
            if (self._limite_saques > 0):
                print(" Erro na operação, limite de saques alcançado!!\n\n")
            else:
                print(" Erro na operação, só é possível sacar valores menores que R$ 500,00!!\n\n")
    
    def depositar(self, valor) -> bool:
        print("\n\nDepósito:", end='')
        if (super().depositar(valor)):
            print(" Operação concluida com sucesso!!\n\n")
        else:
            print(" Erro na operação!!\n\n")
        
   
    def __str__(self) -> str:
        return f'Numero: {super().getNumero()} - Tipo: CC - Saldo: R$ {super().saldo():.2f}'

