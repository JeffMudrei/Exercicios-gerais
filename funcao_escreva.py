def escreva(txt):
    a = len(txt) + 4
    print('~'* a)
    print(f'  {txt}')
    print('~'*a)


txt = input("Escreva seu texto: ").title()
escreva(txt)