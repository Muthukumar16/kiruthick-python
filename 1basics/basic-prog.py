# Write a menu driven program in Python to check whether the number is Armstrong, check whether the number is prime and check whether the number is palindrome
# Check for armstrong number
n= int(input("Enter a number: "))
l=n
sum=0 
z= len(str(n))
while n>0:
    digit=n%10
    sum+=digit**z
    n=n//10
if sum==l:
    print("It is an armstrong number")
else:
    print("Not an armstrong number")
# Check for palindrome
a= str(l)
if a[::-1]==a:
    print("It is a palindrome")

else:
    print("Not a palindrome")
# Prime nor prime number
if l%2==0:
    print("It is not a primr number.")
else:
    print("Prime number")