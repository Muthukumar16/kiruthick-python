# String Manipulation

# Display reverse order
str1 = input("Enter a string: ")
print("The ", str1, "in reverse order is:")

length = len(str1)
for index in range(-1, (-length-1), -1):
    print(str1[index], end=" ")

# O/P: Enter a string: Kiryu
# The  Kiryu in reverse order is:
# n o h t y P

# Forward and Reverse indexes
print("\n")
fIndex = 0
for rIndex in range(-1, (-length-1), -1):
    print(str1[rIndex], "\t", str1[fIndex])
    fIndex += 1
# O/P:
# n 	 P
# o 	 y
# h 	 t
# t 	 h
# y 	 o
# P 	 n


