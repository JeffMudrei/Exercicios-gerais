def recurse(n, s):
    '''Função recurse.
    incrementa o valor de n em s e subtrai 1 do valor de n.
    Quando o n se iguala a zero imprime o valor de s (soma dos 'n' de cada loop)'''
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(4, 0)