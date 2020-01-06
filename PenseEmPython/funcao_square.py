import turtle

def poligon(a, l, d):
    '''Função Poligon:
    Desenha um polígono de 'n' lados informados pelo usuário'''
    flecha = turtle.Turtle()
    for i in range(l):
        flecha.fd(d)
        flecha.lt(180-a)


d = int(input("Informe o valor, em pixels, do lado do poligono regular: "))
l =  int(input("Informe o valor de lados do poligono regular: "))
a = ((l-2)*180)/l
print(a)
poligon(a, l, d)
turtle.mainloop()
    