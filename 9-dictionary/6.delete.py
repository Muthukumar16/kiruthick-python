# Example to delete elements using `del`

Emp1 = {'name': 'Kiryu', 'age': 17}
print(Emp1)
# O/P: {'name': 'Kiryu', 'age': 17}

del Emp1['age']
print(Emp1)
# O/P: {'name': 'Kiryu'}

# Example to nested elements
EmpNested = {'Kiryu': {'age': 17}, 'Muthu': {'age': 50}}
print(EmpNested)
# O/P: {'Kiryu': {'age': 17}, 'Muthu': {'age': 50}}

del EmpNested['Kiryu']['age']
print(EmpNested)
# O/P: {'Kiryu': {}, 'Muthu': {'age': 50}}

# :Exceptional Flow:
del EmpNested
#print(EmpNested)
# O/P: NameError: name 'EmpNested' is not defined

del Emp1['age']
#print(Emp1)
# KeyError: 'age'

# Example to delete elements using `pop()`

