# Write a program in Python to print the Fibonacci series up to specified terms.
n= eval(input("Enter a number: "))

n1=0
n2=1
count=0

if n<0:
    print("Please enter a positive integer.")
elif n==1:
    print("The Fabiano series of the number is:")
    print(n)

else:
    print("Series upto the number is: ")
    while count<n:
        print(n1)
        nth= n1+n2

        n1=n2
        n2= nth
        count+=1