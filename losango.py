def centraliza(n, l):
    '''Função centraliza.
    centraliza os astrríscos na linha'''

    x = int((n-l)/2)
    print(f'-'*x + '*'*l + '-'*x)

num = int(input("Informe um numero impar: "))

if num%2 == 1:
    for i in range (1, num, 2):
        centraliza(num, i)
    print(f'*'*9)
    for i in range((num-2), 0, -2):
        centraliza(num, i)
else:
    print('Numero informedo não é ímpar!')
