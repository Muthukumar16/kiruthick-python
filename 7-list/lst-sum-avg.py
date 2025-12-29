# Write a menu driven program in Python to reverse the list, find the sum of elements of list, and find average and standard deviation.

a = int(input("Enter the maximum no. of element: "))
list = []

for i in range(a):
  x = int(input("Enter an element. "))
  list.append(x)
print("The original list : " + str(list))
b = sum(list)
mean = b / a
variation = sum([((x - mean)**2) for x in list]) / a
deviation = variation**0.5

print("reversed list is:", list[::-1])
print("Sum of the list is:", b)
print("Average of the list is:", mean)
print("Standard deviation of ths list is  is : " + str(deviation))
