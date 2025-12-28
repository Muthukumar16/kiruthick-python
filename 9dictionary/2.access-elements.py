### Accessing Elements

# Syntax <dictionary-name> [<key>]
# Ex:
teachers = {"ComputerScience": "Sri Vidya"}
print(teachers["ComputerScience"])
# O/P: Sri Vidya

vowels = {"v1": "a", "v2": "b", "v3": "c", "v4": "d", "v5": "e"}
print("vowels v1: ", vowels["v1"])
# O/P: vowels v1:  a
print("vowels ", vowels)
# O/P: vowels  {'v1': 'a', 'v2': 'b', 'v3': 'c', 'v4': 'd', 'v5': 'e'}
#print("vowels v1: ", vowels["v10000"]) # Invalid key's
# O/P: KeyError: 'v10000'

# Access via Conditional
marks = {"RollNo1": 75, "RollNo2": 90, "RollNo3": 50}
if marks["RollNo2"] > 75:
    print("RollNo2 is greater than 75")
else:
    print("RollNo2 is less than 75")
# O/P: RollNo2 is greater than 75

# Traversing a Dictionary Syntax: for <item> in <dict>
# Ex:
for key, value in marks.items():
    print(key, value)
# O/P:
# RollNo1 75
# RollNo2 90
# RollNo3 50

# Access without Loops
print(marks.keys())
print(marks.values())
#O/P:
# dict_keys(['RollNo1', 'RollNo2', 'RollNo3'])
# dict_values([75, 90, 50])

# Converts keys() and values() using list()
print(list(marks.keys()))
print(list(marks.values()))
#O/P:
# ['RollNo1', 'RollNo2', 'RollNo3']
# [75, 90, 50]

# `in` and `not in` operator
if 99 in marks.values():
    print("99 in marks")
else:
    print("99 not in marks")
# O/P: 99 not in marks