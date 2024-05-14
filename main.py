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
    
    print(f" Saque ".center(20, '-'))
    valor: int = int(input("Valor: R$ "))

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

    return saldo, extrato

def deposito(saldo, valor, extrato):
    print(8*"-" + " Deposito " + 8*"-")
    valor: int = int(input("Valor: R$ "))
    if valor <= 0:
        print(f"Valor inválido.\n{30*"-"}")
    else:
        print("Valor depositado com sucesso.")
        saldo += valor
        depositos.append(valor)
        print(f"Saldo atual: R$ {saldo}.00\n{30*"-"}")
        extrato += '|' + f"Depósito: R$ {valor}.00".ljust(50, '-') + '|\n'
    return saldo, extrato

def extrato(saldo, extrato):
    extrato += "\n|" + f" Saldo em conta: R$ {saldo}.00 ".center(50, '-') + f"|\n{50*'-'}"
    print(extrato)

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

while True:
    opcao: int = int(input(menu))

    if opcao == 1:
        
            
    

    elif opcao == 2:
        print(f"{8*"-"} Saque {8*"-"}")
        valor: int = int(input("Valor: R$ "))

        if valor > saldo or numero_saques == LIMITE_SAQUES or valor > limite:
            if valor > saldo:
                print(f"Erro na operação: Valor indisponivel em conta.\n{30*"-"}")
            elif numero_saques == LIMITE_SAQUES:
                print(f"Erro na operação: Quantidade de saques diários atingido.\n{30*"-"}")
            elif valor > limite:
                print(f"Erro na operação: Valor acima do limite de saque permitido.\n{30*"-"}")
        else:
            print("Valor sacado com sucesso.")
            saldo -= valor
            saques.append(valor)
            numero_saques += 1
            print(f"Saldo atual: R$ {saldo}.00\nNumero de saques realizados hoje: {numero_saques}\n{30*"-"}")

    elif opcao == 3:
        print(f" Extrato ".center(30, '-'))
        extrato += '|' +" Saques ".center(30, '-') + '|\n'
        for valor in saques:
            extrato += '|' + f"R$ {valor}.00".ljust(30, '-') + '|\n'
        
        extrato += "\n|" + " Depositos ".center(30, '-') + '|\n'
        for valor in depositos:
            extrato += '|' + f"R$ {valor}.00".ljust(30, '-') + '|\n'
        
        extrato += "\n|" + f" Saldo em conta: R$ {saldo}.00 ".center(30, '-') + f"|\n{30*'-'}"

        print(extrato)

    elif opcao == 4:
        break 

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")