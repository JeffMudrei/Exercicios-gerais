def is_triangle(a,b,c):
    if a+b < c or a+c < b or b+c < a:
        print("It's not a triangle.")
    else:
        print("It's a triangle. ")

a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

is_triangle(a,b,c)