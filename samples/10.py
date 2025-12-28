# Write a program to print factorial of a number using both while and for loop.
x= int(input("Enter a number whose factorial you want to find: "))
factorial= 1
if x<0:
    print("No factorial for negetive number. ")
elif x==0:
    print("Factorial of 0 is 1")

else:
    for i in range(1, x+1):
        factorial = factorial*i
print("Factorial of ",x,"is",factorial)
