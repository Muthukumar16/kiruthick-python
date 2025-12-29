# Example to nested elements

Employee = {'Kiryu': {'age': 17}, 'Muthu': {'age': 50}}
print(Employee)

#To access nested elements using 2D array:
for key in Employee:
    print("Employee", key, ":")
    print("Age:", Employee[key]['age'])