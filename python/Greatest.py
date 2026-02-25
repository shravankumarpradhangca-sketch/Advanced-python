#program to the greatest among three unequal roots

a = float (input("Enter firsty number: "))
b = float (input("Enter second number: "))
c = float (input("Enter third number: "))

if a>b and a>c:
    print("Greatest number is:", a)
elif b>a and b>c:
    print("Greatest number is:", b)
else:
    print("Greatest number is:", c)