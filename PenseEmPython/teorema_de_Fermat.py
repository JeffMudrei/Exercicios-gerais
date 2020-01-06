def check_fermat(a, b, c, n):
    if a**n + b**n == c**n:
        print("Goddamn, Fermat was wrong!!!!")
    else:
        print("Goddamn, Fermat is right!!")


print('-'*40)
print("Let's check Fermat's theorem. 'a^n + b^n != c^n', if n>=2")
print('-'*40)
a = int(input("Enter the first number to check the theorem: "))
b = int(input("Enter the second number to check the theorem: "))
c = int(input("Enter the third number to check the theorem: "))
n = int(input("Enter the 'n' number to check the theorem: "))
if n>=2:
    check_fermat(a,b,c,n)
else:
    print("Invalid value.")


