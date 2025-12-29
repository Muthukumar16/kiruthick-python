# Write a program in Python to search a specified element in a given list.
list1= []
for i in range(5):
    x=input("Enter a element: ")
    list1.append(x)
print("You entered this list:", list1)
y= input("Enter the element you want to find: ")

for j in range(len(list1)):
    if y==list1[j]:
        print("Present in list")
        break
else:
    print("not present in list")
        