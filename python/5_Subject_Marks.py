import math

# Program to calculate the total marks and average of 5 subjects

m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))
m4 = int(input("Enter marks for subject 4: "))
m5 = int(input("Enter marks for subject 5: "))

total = m1 + m2 + m3 + m4 + m5

percentage = (total / 500) * 100
print("Total marks: ",total)
print("Percentage: ", percentage)

if  percentage >= 90:
    print("Result: A Grade")
elif percentage >= 80:
    print("Result: B Grade")
elif percentage >= 70:
    print("Result: C Grade")
elif percentage >= 60:
    print("Result: D grade")
elif percentage >= 40:
    print("Result: E Grade")
else:
    print("Result: Fail")