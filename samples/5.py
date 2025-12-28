# Write a python program to take length and breadth of rectangle and print area and perimeter.

length= int(input("Enter the length of rectangle: "))
bredth= int(input("Enter the bredth of rectangle: "))

area= length*bredth
perimeter = 2*(length+bredth)

print("Area of rectangle is:", area)
print("Perimeter of rectangle is:", perimeter)