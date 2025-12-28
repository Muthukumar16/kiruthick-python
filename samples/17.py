x= input("Enter a string: ")
# To find length of a string
print("Length of the string is", len(x))
# Copy a string
z= "" +x
print("Copied string is", z)
# Concat two strings.
y= input("Enter another string: ")
a= x+y
print(a)

# Compare two strings
print(x==y)
print(x>y)
print(x<y)
print(x!=y)

# Reverse a string
b= x[::-1]
print("Reversed string is", b)

# Check if string is a palindrome.
if x[::-1]==x:
    print("It is a palindrome")

else:
    print("Not a palindrome")