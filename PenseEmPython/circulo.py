import turtle

def circle(r):
    t = turtle.Turtle()
    t.circle(r)

r = int(input("Informe o raio do circulo: "))
circle(r)
turtle.mainloop()
