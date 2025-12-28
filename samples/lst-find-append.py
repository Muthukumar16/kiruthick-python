# Write a program in Python to find the largest and smallest element in a list.

list1= []
for i in range(5):
    x=int(input("Enter a element: "))
    list1.append(x)
print("You entered this list:", list1)

y=max(list1)
z=min(list1)
print("Minimum value of the list is", z)
print("Maximum value of the list is", y)