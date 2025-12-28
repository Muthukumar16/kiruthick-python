### Multiple ways to create Dictionary

### Initialize with empty values
Emp1 = {}
print (Emp1)
# O/P: {}

### Initialize with key & values
Emp2 = {"name":"Kiryu","subject":"CS", "age": 17}
print (Emp2)
# O/P: {'name': 'Kiryu', 'subject': 'CS', 'age': 17}

###--------------------Constructor-------------------------------- #####

Emp3= dict()                                     ### Using Constructor
print (Emp3)
# O/P: {}

### Using Dictionary constructor
Emp4 = dict(salary=50000, age=17, name='Kiryu')  ### equal operator (=)
print(Emp4)
# O/P: {'salary': 50000, 'age': 17, 'name': 'Kiryu'}

Emp5 = dict(zip(('name','age'),('MUTHU', 50)))   ### Using zip
print(Emp5)
# O/P: {'name': 'MUTHU', 'age': 50}

Emp6 = dict([['name','Elayarani'],['age', 47]])  ### Using List
print(Emp6)
# O/P: {'name': 'Elayarani', 'age': 47}

Emp7 = dict((('name','Sai'),('age', 2)))        ### Using Tuples
print(Emp7)
# O/P: {'name': 'Sai', 'age': 2}

