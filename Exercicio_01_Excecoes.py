
class ValorInvalidoError(Exception):
    '''Erro para valor negativo'''
    pass

class InvalidOption(Exception):
    '''Erro para opção do menu inválida'''
    pass

def erro_valor_negativo(entrada):
    '''Função para checar valor de entrada negativo
    Se o valor for negativo retorna a mensagem de erro.'''
    if entrada <= 0:
        raise InvalidOption(f"O valor não pode ser negativo, valor informado: R$",entrada)
    return (entrada)

def erro_valor_op(opcao):
    '''Função para checar a opção
    Se a opçao não estiver correta pede uma nova opção.'''
    if opcao not in (range(1,5)):
        raise InvalidOption(f"Opção inválida escolha uma opção válida.")
    return (opcao)


class Correntista:
    '''Definindo o interador'''
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo
        self.historico = []
        self.index = 0
    def nome(self):
        return self.__nome

    def __iter__(self):
        return self

    def __str__(self):
        return "Nome: " + str(self.__nome) +"\nSaldo: R$" + str(self.__saldo)

    '''Index igual ao tamanho do historico, quando iguala para'''

    def __next__(self):
        if self.index == len(self.historico):
            raise StopIteration
        self.index = self.index + 1
        return self.historico[self.index-1]


    def deposito(self, valor):
        '''Função depósito
        Realiza depositos e soma com o saldo existente.
        Retorna erro se for valor inválido.'''
        if valor < 0:
            raise ValorInvalidoError("Valor inválido, informe um valor válido: R$")
        else:
            self.__saldo += valor
            self.historico.append(['Deposito', valor])
            print('Valor depositado: R$',valor)

    def saque(self, valor):

        '''Função saque:
        Realiza saque subtraindo o valor do saldo
        Retorna erro para valores negativos e se o valor for maior que o saldo.'''

        if valor > self.__saldo:
            raise ValorInvalidoError(f"Valor de saque (R${valor}) maior que valor de saldo(R${self.__saldo})")
        elif valor < 0:
            raise ValorInvalidoError(f"Valor de saque inválido (R${valor}), informe um valor válido: R$")
        else:
            self.__saldo -= valor
            self.historico.append(["Saque", valor])
            print(f'Valor sacado: R$', valor)






v = 0
print('-'*40)
nome = input("Digite o nome do correntista: ")
print('-'*40)
saldo = float(input("Informe o saldo inicial: "))
print('-'*40)
c = Correntista(nome,saldo)
op = 's'
clientes = []


while True:
    try:
        operacao = int(input('Digite a opção:\n1 - SAQUE  \n2 - DEPOSITO \n3 - EXTRATO \n4 - SAIR '))
        erro_valor_op(operacao)

        if operacao == 1:
            print('='*30)
            v = float(input("Digite o valor para saque: "))
            saida = erro_valor_negativo(v)
            c.saque(v)
            print('='*30)
        if operacao == 2:
            print('=' * 30)
            v = float(input("Digite o valor para deposito: "))
            saida = erro_valor_negativo(v)
            c.deposito(v)
            print('='*30)
        if operacao == 3:
            print('=' * 30)
            for i in c:
                print(i)
            print(c)
            print('='*30)
        if operacao == 4:
            print('=' * 30)
            print('FIM')
            break

    except ValorInvalidoError as cls:
        print("Erro, ", cls)

    except InvalidOption as vlr:
        print("Erro durante a operação.", vlr)





