# Create Tuples

t = (1, 2, 3)
print(t)
# O/P: (1, 2, 3)
tChar = ('a', 'b')
print(tChar)
# O/P: ('a', 'b')
tMixed = ('a', 1, 3.5, 2, 'zero')
print(tMixed)
# O/P: ('a', 1, 3.5, 2, 'zero')

#### Create Empty tuple using constructor method
tCons = tuple()
print(tCons)
# O/P: ()

#### Single element (note the comma!)
tComma = 3,
print(tComma)
# O/P: (3,)

#### Long tuples
tSQRS = (0, 1, 4, 9, 16, 25, 30, ...)
print(tSQRS)
# O/P: (0, 1, 4, 9, 16, 25, 30, Ellipsis)

#### Nested tuples
tNested = (1, 2, (3, 4))
print(tNested)
# O/P: (1, 2, (3, 4))

#### Creating from existing sequence
tStr = tuple("hello")
print(tStr)
# O/P:  ('h', 'e', 'l', 'l', 'o')

#### From list
tLst = tuple([1, 2, 3])
print(tLst)
# O/P: (1, 2, 3)

#### From dictionary
tDict = tuple({'1': '11', 2: '2'})
print(tDict)
# O/P: ('1', 2)

#### Input from keyboard
tInput = tuple(input("Enter tuple elements: "))
print(tInput)
# I/P: Enter tuple elements: 1234567
# O/P: ('1', '2', '3', '4', '5', '6', '7')