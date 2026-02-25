x = int(input("Enter a number:"))
y = int(input("Enter a number:"))
z = int(input("Enter a number:"))
if (x >= y) and (x >= z):
    print(f"{x} is the largest number.")
elif (y >= x) and (y >= z):
    print(f"{y} is the largest number.")
else:
    print(f"{z} is the largest number.")
