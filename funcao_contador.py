from time import sleep

def contador(inicio, fim, passo):
    print(f'contando de {inicio} até {fim} de {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += passo
        print("FIM")
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= passo
        print("FIM")


'''Programa principal'''
inicio = int(input('Informe o inicio: '))
fim = int(input('Informe o final: '))
passo = int(input('Informe o passo: '))
contador(inicio, fim, passo)
