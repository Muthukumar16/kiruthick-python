# Write a program in Python to check whether a character is an alphabet or not and also check its case.

x= input("ENter a string: ")

if x.isalpha() and x.islower():
    print("It is an alphabet with lower case")
elif x.isalpha() and x.isupper():
    print("It is an alphabet with upper case")
else:
    print("It is not an alphabet")