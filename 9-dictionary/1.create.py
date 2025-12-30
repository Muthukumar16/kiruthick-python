### Syntax

### <dictionary-name> = {<key>: <value>, <key>: <value>, ...}

### Example
teachers = {"Role#":21, "Name":"Kiryu", "Subject": "Maths"}
print(teachers)
# O/P: {'Role#': 21, 'Name': 'Kiryu', 'Subject': 'Maths'}

dictTupleKey = {(1,2): "abc"}
print(dictTupleKey)
# O/P: {(1, 2): 'abc'}

# Exceptional Flow
#dictListKey = {[1,2]: "def"}
#print(dictListKey)
# O/P: TypeError: cannot use 'list' as a dict key (unhashable type: 'list')

# Creating Dictionary from keys - the fromkeys() Method
# Basic keys with default values
nd = dict.fromkeys([1,2,3,4])
print(nd)
# O/P: {1: None, 2: None, 3: None, 4: None}

# Keys with common values
nd1 = dict.fromkeys([1,2,3,4], 1000)
print(nd1)
# O/P: {1: 1000, 2: 1000, 3: 1000, 4: 1000}

# Tuples
# Basic keys with default values
nd2 = dict.fromkeys((1,2,3,4))
print(nd2)
# O/P: {1: None, 2: None, 3: None, 4: None}

# Keys with respective value arguments
nd3 = dict.fromkeys((1,2,3), (100,200,300))
print(nd3)
# O/P: {1: (100, 200, 300), 2: (100, 200, 300), 3: (100, 200, 300)}

