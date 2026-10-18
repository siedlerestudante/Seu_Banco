class ContaBancaria:
    def __init__(self, titular, saldo):

        self.titular = titular
        self.saldo = saldo

    def qnt_saldo(self):
        print(f"O saldo é de {self.saldo:.2f}")

    def depositar(self):
        valor = float(input("Quanto gostaria de depositar? "))
        self.saldo += valor
        print(f"O saldo agora do titular {self.titular} é de R$ {self.saldo:.2f}")

    def nome_titular(self):
        print(f"o titular é {self.titular}")


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo,):
        super().__init__(titular, saldo)

    def aplicar_juros(self):
        self.saldo *= 1.01
        print(f"com a taxa de 1%, o saldo agora é de {self.saldo:.2f}")

    def mostrar_juros():
        print("O juros é de 1%")

print("Bem-Vindo ao Seu-Banco, o seu banco")

t1 = ContaPoupanca(titular = str(input("qual o nome do titular? ")),saldo = (int(input("Qual o valor do seu saldo atual? "))))

def funcoes():
    print(""" 
--------------------------
1 -> Nome do Titular
2 -> Saldo Disponivel
3 -> Depositar Dinheiro
4 -> Mostrar Juros Atual 
5 -> Aplicar Juros 
6 -> Sair do Seu-Banco
--------------------------


""")


option = 0

while option == 0:

    funcoes()

    try:
        option += int(input("Qual função gostaria de utilizar? " ))
    except ValueError:
        print("Digite apenas números!")
        option = 0
        continue

    if option == 1:
        t1.nome_titular()
        option = 0

    elif option == 2:
        t1.qnt_saldo()
        option = 0

    elif option == 3:
        t1.depositar()
        option = 0

    elif option == 4:
        ContaPoupanca.mostrar_juros()
        option = 0

    elif option == 5: 
        t1.aplicar_juros()
        option = 0

    elif option == 6:
        print("Fechando o Seu-Banco...")
        break

    else: print("não há essa opção, digite uma opção existente")
    option = 0
