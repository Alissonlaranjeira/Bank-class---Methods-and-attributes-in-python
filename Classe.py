class Conta:

    #Construtor:    (atributos)
    def __init__(self,numero,titular,saldo,limite):

        #__ indica que vc n deve alterar diretamente os atributos do objeto,o certo é só com os metodos!!!
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    #Metodos:
    def extrato(self):  # imprimir o extrato
        print("Saldo de R$ {}  do titular {}".format(self.__saldo,self.__titular.title()))
    def deposita(self, valor):  # inserir dinheiro na conta
        self.__saldo = self.__saldo + valor

    def __pode_sacar(self,valor): #privado
        return valor <= self.__saldo + self.__limite #privado

    def saca(self, valor):  # tirar dinheiro na conta
        if(self.__pode_sacar(valor)):
            self.__saldo = self.__saldo - valor
        else:
            print("O valor de {} reais passou o limite".format(valor))

    def transfere (self,valor,destino): #pega dinhero do self e coloca no destino: c1.tranfere(10,c2) coloca 10 reais de c1 em c2
        self.saca(valor) #origem
        destino.deposita(valor)

    #get (retorna os atributos):
    @property  # RETORNAR - n usar parenteses ao chamar
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    #Método estativo,nao precisa de objeto
    @staticmethod
    def codigo_banco():
        return {"Banco do Brasil":"001","Caixa":"104 ","Bradesco":"237"} #diciario

    #set (alterar os atrivutos):
    @limite.setter  # ALTERAR
    def limite(self,novo):
        self.__limite = novo

class client:
    #construtor:
    def __init__(self,nome):
        # atributos:
        self.__nome=nome
    def get_nome(self):
        return self.__nome.title() #title() retorna a primeira letra maiuscula.

    #SEM PARENTESES:
    @property   #RETORNAR
    def nome(self): #retorna o nome
        return self.__nome.title() #title() retorna a primeira letra maiuscula.
    @nome.setter #ALTERAR
    def nome(self,nome): #muda o nome
        self.__nome = nome

print("----Criando uma conta----")
numero = input("Insira o Número da conta:")
titular = input("Insira o nome do titular:")
saldo = input ("Insira o saldo inicial:")
limite = input("Insira o limite:")
c = Conta(numero,titular,saldo,limite)

i=0
while(i>3 or i<1):

    print("----Operações disponiveis----")
    print("Extrato        (1)")
    print("Depósito       (2)")
    print("Sacar          (3)")

    i=int(input("\nSelecione a operação:"))

    if(i==1):
        c.extrato()
    elif(i==2):
        valor = input("Insira o valor a ser depositado: ")
        c.deposita(valor)
    elif(i==3):
        valor = input("Insira o valor a ser sacado: ")
        c.saca(valor)

    print ("\nDeseja fazer outra operação?")
    print("Sim (0)")
    print("Não (1)")
    e = int(input())
    if(e == 0):
        i=0
    elif(e == 1):
        break