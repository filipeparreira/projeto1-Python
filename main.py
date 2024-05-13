'''
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
'''


menu = '''
    [1] Depositar
    [2] Sacar 
    [3] Extrato
    [4] Sair

=> '''

saldo: int = 0
limite: int = 500
extrato: str = ""
numero_saques: int = 0
LIMITE_SAQUES: int = 3
saques: int = []
depositos: int = []

while True:
    opcao: int = int(input(menu))

    if opcao == 1:
        print(8*"-" + " Deposito " + 8*"-")
        valor: int = int(input("Valor: R$ "))
        if valor <= 0:
            print("Valor inválido.")
        else:
            print("Valor depositado com sucesso.")
            saldo += valor
            depositos.append(valor)
            print(f"Saldo atual: R$ {saldo}.00\n{30*"-"}")
            
    
    elif opcao == 2:
        print("Saque")

    elif opcao == 3:
        print("Extrato")

    elif opcao == 4:
        break 

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")