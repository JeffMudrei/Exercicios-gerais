import turtle
bob = turtle.Turtle()
print(bob)
bob.fd(100) #fd desloca o Turtle para frente (distancia em pixels), bk para tras.
bob.lt(90) #lt vira a esquerda, rd a direita, antulo em graus.
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
for i in range(4): #utiliza o medodo for para refazer o quadrado.
    bob.fd(100)
    bob.lt(90)
turtle.mainloop()
