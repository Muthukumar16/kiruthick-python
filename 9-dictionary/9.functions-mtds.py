# len() Function
emp = {'name':'Kiryu', 'age': 17, 'city': 'Bangalore', 'country': 'India'}
print(len(emp))
# O/P: 4

# Accessing Items

# get()
print(emp.get('city'))
# O/P: Bangalore

print(emp.get('test', "Not yet defined"))
# O/P: Not yet defined

# items()
seqTuples = emp.items()
for tuple in seqTuples:
    print(tuple)
# O/P:
# ('name', 'Kiryu')
# ('age', 17)
# ('city', 'Bangalore')
# ('country', 'India')

myKeyValue = emp.items()
for key, value in myKeyValue:
    print(key,":",value)

# O/P:
# name : Kiryu
# age : 17
# city : Bangalore
# country : India

# keys()
print(emp.keys())
# O/P: dict_keys(['name', 'age', 'city', 'country'])

# values()
print(emp.values())
# O/P: dict_values(['Kiryu', 17, 'Bangalore', 'India'])