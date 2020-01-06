import turtle
def koch(x, n):
    for i in range(n):
        t.fd(x / 3)
        t.lt(60)
        t.fd(x / 3)
        t.rt(120)
        t.fd(x / 3)
        t.lt(60)
        t.fd(x / 3)
        t.rt(-60)

t = turtle.Turtle()
koch(30, 20)

turtle.mainloop()


