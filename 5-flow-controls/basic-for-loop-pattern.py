# Write a menu driven program in Python to print the given patterns (star,letters, number).
# (1) Star pattern
# x= int(input("Enter a number: "))

# for i in range(0,x):
#     for j in range(0, i+1):
#         print('*', end="")
#     print("")

# # (2) A AB ABC pattern
# x= int(input("Enter a number: "))
# str= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for i in range(0,x):
#     for j in range(0, i+1):
#         print(str[j], end="")
#     print("")

# (3)1 22 333 4444 pattern
x= eval(input("Enter a number: "))

for i in range(1,x+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print("")
