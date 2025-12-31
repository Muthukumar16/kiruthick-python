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

#del Emp1['age']
#print(Emp1)
# KeyError: 'age'

# Example to delete elements using `pop()`
Subject = {1: 'Maths', 2: "Computer", 3: "Physics", 4: "Chemistry", 5: "English"}
print(Subject)
# O/P: {1: 'Maths', 2: 'Computer', 3: 'Physics', 4: 'Chemistry', 5: 'English'}
print(Subject.pop(1))
# O/P: Maths
print(Subject)
# O/P: {2: 'Computer', 3: 'Physics', 4: 'Chemistry', 5: 'English'}

#Example to delete elements using `popitem()` - LIFO (Last In First Out)
print(Subject.popitem())
# O/P: (5, 'English')
print(Subject)
# O/P: {2: 'Computer', 3: 'Physics', 4: 'Chemistry'}

# clear() - remove all the elements and object/dictionary become empty elements
print(Subject.clear())
# O/P: None
print(Subject)
# O/P: {}