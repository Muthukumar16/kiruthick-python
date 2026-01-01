## TUPLES
#### What is a Tuple?
A tuple is a sequence that is used to store a collection of values of any type. Tuples are immutable (cannot be changed) and Python creates a fresh tuple when we make changes to any element.

#### Key Characteristics:
- Immutable (can't change values)
- Non-modifiable
- Ordered sequence
- Can contain mixed data types

#### Creating & Accessing Tuples
#### Creating Tuples
```python
# Syntax
T = ()  # Empty tuple
T = (<v1>,<v2>)  # Single element tuple (comma required!)
```
Examples: [Create Tuples](1.create.py)

### Tuple Creation Syntax
| S.No | Method                          | Syntax Example                                      | Notes                                |
|------|---------------------------------|-----------------------------------------------------|--------------------------------------|
| 1    | Multiple elements               | `T = (element1, element2, element3, ...)`           | Standard tuple creation              |
| 2    | Empty tuple (constructor)       | `T = tuple()`                                       | Creates an empty tuple               |
| 3    | Single-element tuple            | `T = (element,)` or `T = element,`                  | Comma is required for single element |
| 4    | Long tuple                      | `T = (element1, element2, element3, ...)`           | Can contain many elements            |
| 5    | Nested tuple                    | `T = (element1, element2, (nested1, nested2))`      | Tuples inside tuples                 |
| 6    | From existing sequence          | `T = tuple(sequence)`                               | Converts sequence to tuple           |
| 7    | From list                       | `T = tuple([list_elements])`                        | Converts list to tuple               |
| 8    | From dictionary (keys only)     | `T = tuple({key1: value1, key2: value2, ...})`      | Extracts keys as tuple               |
| 9    | From keyboard input             | `T = tuple(input("Enter tuple elements: "))`        | Input converted into tuple of chars  |

### Tuple Creation Syntax (Additional)

- Create tuple using `eval(input())` to preserve datatypes  
  `T = eval(input())`

## Accessing Tuples
#### Tuple Forward and Backward Indexing:

| Forward       | 0  | 1  | 2  | 3  | 4  |
|---------------|----|----|----|----|----|
| **Elementes** | **a**  | **e**  | **i**  | **o**  |**u** |
| Backward      | -5 | -4 | -3 | -2 | -1 |


- Store a reference at the each index instead of single character as in strings
- Each individual item stored somewhere in memory
#### Important Notes:

### Tuple Operations

| Operation              | Syntax / Operators | Description                |
|------------------------|--------------------|----------------------------|
| Length                 | `len(T)`           | Returns the number of elements in the tuple |
| Membership             | `in`, `not in`     | Checks if an element exists in the tuple    |
| Concatenation          | `+`                | Combines two tuples into one                |
| Replication            | `*`                | Repeats the tuple elements multiple times   |

- Difference from List: Tuples are immutable

#### How to Make Tuples Mutable
- Since tuples are immutable, to modify them:
- num = ([1, 2, 3], [4, 5, 6])
- num[1] = [1, 2, 0]    ❌ Immutable - Type Error
- num[0][2] = 0         ✓ Mutable - Changes inner list

- print(num)  # O/P: ([1, 2, 0], [4, 5, 6])

#### Three ways to create a true copy of a list:
- list()
- copy()
- Storing all elements of list using list slice with copy

```python
# Example: 
lstCopy = [1,2,3]
lstCpy = lstCopy[:]
print(lstCpy)
# O/P: [1, 2, 3]
```


#### Tuple Built-in Functions & Methods

| Function | Syntax                  | Description                                |
|----------|-------------------------|--------------------------------------------|
| len()    | `len(<tuple>)`          | Returns the length of the tuple            |
| max()    | `max(<tuple>)`          | Returns the maximum element                |
| min()    | `min(<tuple>)`          | Returns the minimum element                |
| sum()    | `sum(<tuple>)`          | Returns the sum of all elements            |
| index()  | `<tuple>.index(<item>)` | Returns the index of the specified element |
| count()  | `<tuple>.count(<item>)` | Returns the count of an item               |


#### sorted() - Returns a sorted list.
`Syntax: sorted(<iterable>)`
#### tuple() - Constructor method - used to create different types of values.
```python# Syntax: tuple(<seq>)
t = tuple("abc")  
# O/P: ('a', 'b', 'c')
```

#### From list
```python
t = tuple([1, 2, 3])  
# O/P: (1, 2, 3)
```

#### From dictionary
```python
t = tuple({'1': '11', 2: '2'})  
# Output: ('1', 2)
```
#### Deleting Tuples
```python
# Syntax: del <tuplename>
t1 = (5, 7, 9)
del t1
print(t1)  
# Output: NameError - not defined
```

### Tuple Operations

| Operation   | Syntax / Example            | Description / Notes                                                                                                                                                     |
|-------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Join (+)    | `T1 + T2`                   | Concatenates tuples. ⚠️ Both operands must be tuples. <br> - `tuple + number` → ❌ Error <br> - `tuple + list` → ❌ Error <br> - `T1 + (3)` → ❌ Error <br> - `T1 + (3,)` → ✓ Valid |
| Replicate (*) | `T * n`                   | Repeats the tuple elements `n` times.                                                                                                                                   |
| Slicing     | `T[start:stop]`             | Extracts sub-parts of a tuple from `start` index up to `stop-1`.                                                                                                        |
| Slicing with step | `T[start:stop:step]`  | Extracts elements with a step interval. `Example: `T[0:10:2]` → selects every 2nd element.`                                                                              |


#### Comparing Tuples
```python
a = (1, 2, 3)
b = (1, 2, 3)

a == b  # True
c = ('1', '2', '3')
a == c  # False

d = (1, 0, 2, 0, 3, 0)
a == d  # True
```

#### Unpacking Tuples
- Creating a tuple from a set of values is called packing. Creating individual values from a tuple's element is called unpacking.
```python
t = (1, 2, 'A', 'B')
w, x, y, z = t

print(w)  # Output: 1
print(x)  # Output: 2
print(y)  # Output: 'A'
print(z)  # Output: 'B'
```

#### Traversing a Tuple
- Using For Loop
```python 
# Syntax: 
# for <item> in <tuple>:
#     process each item here

T = ('P', 'Y', 'T', 'H', 'O', 'N')
for a in T:
    print(T[a])  

# Output: P Y T H O N
```
- Using For Index in Range
```python 
# Syntax: 
# for index in range(len(T)):
#     process each item here
```
