'''
Parte 1

    Criar um sistema bancario com as operacoes de saque, deposito e extrato

    Deposito: 
        - Deve ser possivel depositar valores positivos 
        - Como essa versao contem somente 1 usuario n eh necessario identificar agencia ou conta
        - Todos os depositos devem ser armazenados em uma variavel 
        - Todos os depositos dever ser exibidos na operacao de extrato
    
    Saque: 
        - Deve permitir realizar 3 saques diarios com limite de 500 reais por saque
        - Caso o usuario nao tenha saldo em conta, exibir uma mensagem informando que nao foi possivel realizar
            o saque por falta de dinheiro.
        - Todos os saques devem ser armazenados em uma variavel para serem exibidos no extrato
    
    Extrato:
        - Listar todos os depositos e saques da conta 
        - No fim da listagem deve exibir o saldo atual da conta
        - Os valores devem ser exibidos no formato R$ xxx.xx

Parte 2
        
    Atualizar o sistema bancario ja criado:
        - Separar as operacoes em funcoes 
            - Sugestao de argumentos para cada funcao 
                - saque(saldo, valor, extrato, limite, numero_saques, limite_saques) = saldo e extrato # Keyword Only
                - deposito(saldo, valor, extrato) = saldo e extrato # Positional Only
                - extrato(saldo **Positional Only, extrato **Keyword Only)
        
            - Implementar mais duas funcoes
                - Criar Usuario 
                - Criar Conta Corrente
                - (Opcional) Criar Listar Contas

            - Criar Usuario:
                - Deve armazenar os usuarios em uma lista 
                - Um usuario tem nome, data de nascimento, cpf, endereco
                - O endereco eh uma string formada por logradouro, numero - bairro - cidade/sigla estado
                - Em cpf, deve ser armazenado somente numeros 
                - Nao pode cadastrar dois usuarios com o mesmo cpf
            
            - Criar Conta Corrente:
                - Deve armazenar as contas em uma lista 
                - Uma conta tem agencia, numero de conta e usuario
                - O numero de conta e sequencial, iniciado em 1 (ou seja, na medida que as contas são criados
                    o numero da conta eh incrementado com base no numero da conta anterior)
                - O numero da agencia é fixo "0001"
                - O usuario pode ter mais de uma conta, mas uma conta pertence somente a 1 usuario 
                - (dica) Para vincular a nova conta a um usuario, utilizar o cpf do mesmo como chave de busca
                - Caso nao encontre o usuario, nao criar a conta
'''

# Segmentando o codigo 
def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo or numero_saques == limite_saques or valor > limite:
        if valor > saldo:
            print(f"Erro na operação: Valor indisponivel em conta.\n{30*"-"}")
        elif numero_saques == limite_saques:
            print(f"Erro na operação: Quantidade de saques diários atingido.\n{30*"-"}")
        elif valor > limite:
            print(f"Erro na operação: Valor acima do limite de saque permitido.\n{30*"-"}")
    else:
        print("Valor sacado com sucesso.")
        saldo -= valor
        saques.append(valor)
        numero_saques += 1
        print(f"Saldo atual: R$ {saldo}.00\nNumero de saques realizados hoje: {numero_saques}\n{30*"-"}")
        extrato += '|' + f"Saque: R$ {valor}.00".ljust(50, '-') + '|\n'

    return saldo, extrato, numero_saques

def deposito(saldo, valor, extrato):
    if valor <= 0:
        print(f"Valor inválido.\n{30*"-"}")
    else:
        print("Valor depositado com sucesso.")
        saldo += valor
        depositos.append(valor)
        print(f"Saldo atual: R$ {saldo}.00\n{30*"-"}")
        extrato += '|' + f"Depósito: R$ {valor}.00".ljust(50, '-') + '|\n'
    return saldo, extrato

def gera_extrato(saldo, extrato):
    extrato += "|" + f" Saldo em conta: R$ {saldo}.00 ".center(50, '-') + f"|\n{50*'-'}"
    print(extrato)


# Novas funcoes
def cria_usuario(user: dict, nome, endereco, data_nascimento, cpf: str, lista_usuarios: list):
    # Atribui os valores ao usuario
    user["nome"] = nome
    user["endereco"] = endereco
    user["data_nascimento"] = data_nascimento
    user["contas"] = list()
    
    if busca_usuario(cpf, lista_usuarios):
        print("Erro na operação: CPF já presente na base de dados.\nUsuário não criado")
    elif cpf.isdigit:
        user["cpf"] = cpf
        # Adiciona o usuario na lista de usuarios
        lista_usuarios.append(user.copy())
    else:
        print("Erro na operação: Informação de CPF inválida!\nUsuário não criado")

    # Retornar a lista de usuarios
    return lista_usuarios
    
def preenche_endereco(endereco, logradouro, numero, bairro, cidade, estado):
    endereco["logradouro"] = logradouro
    endereco["numero"] = numero
    endereco["bairro"] = bairro
    endereco["cidade"] = cidade
    endereco["estado"] = estado
    return endereco

def cria_conta_corrente(user:dict, conta:dict, contas:list, lista_users: list):
    conta["numero_conta"] = len(contas) + 1
    conta["usuario"] = user
    user["contas"].append(conta)
    lista_users.append(user)
    return lista_users

def busca_usuario(cpf, lista_users:list):
    user = list(filter(lambda usuario: usuario["cpf"] == cpf, lista_users))
    lista_users.remove(user)
    return user

def lista_users(lista_users:list):
    print(f" Lista de Usuarios Cadastrados ".center(50, '-'))
    for conta in lista_users:
        print(f"Nome: {conta["nome"]}   Data Nasc.: {conta["data_nascimento"]}  Nº de Contas: {len(conta["contas"])}".center(100))

menu = '''
    [1] Depositar
    [2] Sacar 
    [3] Extrato
    [4] Criar Conta Usuario
    [5] Criar Conta Corrente
    [6] Sair

=> '''

saldo: int = 0
limite: int = 500
extrato: str = f" Extrato ".center(50, '-') + '\n'
numero_saques: int = 0
LIMITE_SAQUES: int = 3
saques: int = []
depositos: int = []
lista_usuarios: list = []
contas: list = []
usuario_end: dict = {"logradouro": "", "numero": "", "bairro": "", "cidade": "", "estado" : ""}
usuario: dict = {"nome" : "", "data_nascimeto" : "", "cpf" : "", "endereco": usuario_end, "contas" : contas}
conta: dict = {"agencia" : "0001", "numero_conta": 0, "usuario": usuario}



while True:
    opcao: int = int(input(menu))

    if opcao == 1:
        print(f" Deposito ".center(20, '-'))
        valor: int = int(input("Valor: R$ "))
        saldo, extrato = deposito(saldo, valor, extrato)           
    

    elif opcao == 2:
        print(f" Saque ".center(20, '-'))
        valor: int = int(input("Valor: R$ "))
        saldo, extrato, numero_saques = saque(limite_saques=LIMITE_SAQUES, saldo=saldo, extrato=extrato, valor=valor, limite=limite, numero_saques=numero_saques)
        
    elif opcao == 3:
        gera_extrato(saldo, extrato=extrato)

    elif opcao == 6:
        break 

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")