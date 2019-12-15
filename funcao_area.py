def areaRetangulo (a,b):
    area = a * b
    print('-'*40)
    print(f'O valor da área do retangulo informado é {area}m²')
    print('-'*40)


a = float(input("Informa o valor do primeiro lado em metros: "))
b = float(input("Informe o valor do segundo lado em metros: "))
areaRetangulo(a , b)