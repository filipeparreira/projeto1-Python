from classes import PessoaFisica, ContaCorrente

cliente1 = PessoaFisica(123456, 'Filipe', 21112001, 'Rua 1, Bairro Teste')
conta1_c1 = ContaCorrente(cliente1, 159)

cliente1.adicionar_conta(conta1_c1)
print(cliente1)

conta1_c1.depositar(1500)
print(cliente1)
conta1_c1.sacar(501)