### Syntex

### <9dictionary-name> = {<key>: <value>, <key>: <value>, ...}

### Example
teachers = {"Role#":21, "Name":"Kiryu", "Subject": "Maths"}
print(teachers)
# O/P: {'Role#': 21, 'Name': 'Kiryu', 'Subject': 'Maths'}

dictTupleKey = {(1,2): "abc"}
print(dictTupleKey)
# O/P: {(1, 2): 'abc'}

dictListKey = {[1,2]: "def"}
print(dictListKey)
# O/P: TypeError: cannot use 'list' as a dict key (unhashable type: 'list')