def intervalo(n):
    return (*range(n), *range(n, -1, -1))


def centraliza(texto, largura, separador=' '):
    return f'{texto:{separador}^{largura}}'


def texto(numeros):
    return ''.join(str(n) for n in numeros)


def linha(n, largura, sep=' '):
    return centraliza(texto(intervalo(n)), largura, sep)


def losango(n, separador=' '):
    largura = n * 2 + 1

    return '\n'.join(linha(n, largura, separador) for n in intervalo(n))

n = int(input('Informe o intervalo impar para o losango: '))
if (n % 2 == 1):
    a = losango(n)
    print(a)
else:
    print('O numero não é impar.')