string = input("Enter a string: ")
reversed_string = string[::-1]

if string == reversed_string:
    print("The given string is a palindrome")

else:
    print("The given string is not a palindrome")