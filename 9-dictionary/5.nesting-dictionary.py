# Example to nested elements

# Add nested elements {<key1>: {<key1.1>: <value1.1>}, <key2>: {<key2.1>: <value2.1>}...}
Employee = {'Kiryu': {'age': 17}, 'Muthu': {'age': 50}}
print(Employee)
# O/P: {'Kiryu': {'age': 17}, 'Muthu': {'age': 50}}

print(Employee['Kiryu']['age'])
# O/P: 17

#To access nested elements using 2D array:
for key in Employee:
    print("Employee", key, ":")
    print("Age:", Employee[key]['age'])
# O/P:
# Employee Kiryu :
# Age: 17
# Employee Muthu :
# Age: 50