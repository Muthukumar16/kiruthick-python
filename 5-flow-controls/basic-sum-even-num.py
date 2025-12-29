# Write a program to print sum of even and odd integers of first n natural numbers.
# Sum of even numbers
n= eval(input("Write a number: "))
sum=0
for i in range(0, n+1, 2):
    sum+=i

print("Sum of even integer of first n terms =", sum)
# Sum of odd numbers
a= eval(input("Write a number: "))
sum2=0
for i in range(0, a+1, 3):
    sum+=i

print("Sum of even integer of first n terms =", sum)