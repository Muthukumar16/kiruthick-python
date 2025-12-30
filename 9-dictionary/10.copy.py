# copy() method -> independent (multiple) reference will be created
Stu = {1: "Kiryu", 2: 'Muthu', 3: 'Elayarani'}
print(Stu)
# O/P: {1: 'Kiryu', 2: 'Muthu', 3: 'Elayarani'}

Stu1 = Stu.copy()
print(Stu1)
# O/P: {1: 'Kiryu', 2: 'Muthu', 3: 'Elayarani'}

Stu1.setdefault(4, 'Sai')
print(Stu1)
# O/P: {1: 'Kiryu', 2: 'Muthu', 3: 'Elayarani', 4: 'Sai'}
print(Stu)
# O/P: {1: 'Kiryu', 2: 'Muthu', 3: 'Elayarani'}
Stu.setdefault(5, 'Test')
Stu1[2] = 'Muthu Kumar'
print(Stu1)
# O/P: {1: 'Kiryu', 2: 'Muthu Kumar', 3: 'Elayarani', 4: 'Sai'}
print(Stu)
# O/P: {1: 'Kiryu', 2: 'Muthu', 3: 'Elayarani', 5: 'Test'}

# Using assignment operator - modification will reflect both references (same value 2 references)
Stu2 = Stu
print(Stu2)
# O/P: {1: 'Kiryu', 2: 'Muthu', 3: 'Elayarani', 5: 'Test'}

Stu2.setdefault(6, 'Test Six')
Stu2[2] = 'Muthu Kumar'
print(Stu2)
# O/P: {1: 'Kiryu', 2: 'Muthu Kumar', 3: 'Elayarani', 5: 'Test', 6: 'Test Six'}
print(Stu)
# O/P: {1: 'Kiryu', 2: 'Muthu Kumar', 3: 'Elayarani', 5: 'Test', 6: 'Test Six'}
