# sorted
str = {41: 'Kiryu', 42: 'Sai', 35: 'Elai', 15: 'Muthu'}
print(str)
# O/P: {41: 'Kiryu', 42: 'Sai', 35: 'Elai', 15: 'Muthu'}

lst = sorted(str)
print(lst)
# O/P: [15, 35, 41, 42]

print(sorted(str, reverse=True))
# O/P: [42, 41, 35, 15]

print(sorted(str.values(), reverse=True))
# O/P: ['Sai', 'Muthu', 'Kiryu', 'Elai']

# Tuples:
dTuples = {(1,2): "One", (3,4): "Two"}
print(sorted(dTuples, reverse=True))
# O/P: [(3, 4), (1, 2)]

str.setdefault("test", 10)
#print(sorted(str))
# O/P: TypeError: '<' not supported between instances of 'str' and 'int'