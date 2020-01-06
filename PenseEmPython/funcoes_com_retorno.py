import math
def area(radius):
    a = math.pi * radius**2
    return a



def maior_menor(a, b):
    if a > b:
        return 0
    else:
        return -1

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2- y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def is_divisible(a, b):
    return a % b == 0

def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False

def factorial(n):
    if n == 0:
        return 1
    else:
        r = factorial(n-1)
        result = n * r
        return result

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def ack(m, n):
    ''' Fução ack
    analisa a função de Ackermann A(m,n)
    sendo m e n inteiros não negativos'''
    if m == 0:
        return n + 1
    elif n == 0 and m > 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1,(ack(m, n-1)))

print (ack(3,4))

