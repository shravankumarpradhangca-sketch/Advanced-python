s1 = int(input("Enter marks of subject 1:"))
s2 = int(input("Enter marks of subject 2:"))
s3 = int(input("Enter marks of subject 3:"))
s4 = int(input("Enter marks of subject 4:"))
s5 = int(input("Enter marks of subject 5:"))
total_marks = s1 + s2 + s3 + s4 + s5
percentage = (total_marks / 250) * 100
if percentage >= 90:
    print("Your grade is : O")
elif percentage >= 80:
    print("Your grade is : E")
elif percentage >= 70:
    print("Your grade is : A")
elif percentage >= 60:
    print("Your grade is : B")
elif percentage >= 50:
    print("Your grade is : C")
elif percentage >= 0:
    print("Your grade is : F")
else:
    print("Invalid grade.")