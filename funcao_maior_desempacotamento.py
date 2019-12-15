def maior (* num):
    cont = maior_num = 0
    print(f'Analisando ')
    for i in num:
        print(f'{i}', end=' ')
        if cont == 0:
            maior_num = i
        else:
            if i > maior_num:
                maior_num = i
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor é {maior_num}')

'''Prorama principal'''

maior(0,1030,1,2,3,4,5,6,7,54,35,6,7,3,5)

