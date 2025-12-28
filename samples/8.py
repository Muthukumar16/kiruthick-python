# Write a program in Python to find minimum of three numbers.
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
c= int(input("Enter a number: "))

smallest =0
if a<b and a<c:
    smallest=a
elif b<c:
    smallest=b
else:
    smallest=c

print(smallest, "is the smallest of the three.")