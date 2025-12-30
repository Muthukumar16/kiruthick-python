# Write a python program to print table of a number in tabular format given by the user as an input.
x= eval(input("Enter a number whose table is to be find: "))

for i in range(11):
    print(x, 'x',i , "=", x*i )