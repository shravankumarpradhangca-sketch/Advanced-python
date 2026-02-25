x = int(input("Enter a number:"))
y = int(input("Enter a number:"))
z = int(input("Enter a number:"))
d = y**2 - 4*x*z

import math
if d>0:
    r1 = (-y+math.sqrt(d))/(2*x)
    r2 = (-y-math.sqrt(d))/(2*x)
    print ("Real roots are", r1, "and", r2)
elif d==0:
    r = -y/(2*x)
    print("only one real root :", r)
else:
    print("No real roots")
