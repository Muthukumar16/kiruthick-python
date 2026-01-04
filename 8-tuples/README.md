## TUPLES
#### What is a Tuple?
- A tuple is a sequence that is used to store a collection of values of any type. 
- Tuples are immutable (cannot be changed) and Python creates a fresh tuple when we make changes to any element.

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
| S.No | Method                    | Syntax Example                                      | Notes                                |
|------|---------------------------|-----------------------------------------------------|--------------------------------------|
| 1    | Empty tuple (constructor) | `T = tuple()`                                       | Creates an empty tuple               |
| 3    | Single-element tuple      | `T = (element,)` or `T = element,`                  | Comma is required for single element |
| 2    | Long/Multiple elements    | `T = (element1, element2, element3, ...)`           | Standard tuple creation              |
| 4    | Nested tuple              | `T = (element1, element2, (nested1, nested2))`      | Tuples inside tuples                 |

### Create from exising collections
| S.No | Method                          | Syntax Example                                      | Notes                                |
|------|---------------------------------|-----------------------------------------------------|--------------------------------------|
| 1    | From existing sequence          | `T = tuple(sequence)`                               | Converts sequence to tuple           |
| 2    | From list                       | `T = tuple([list_elements])`                        | Converts list to tuple               |
| 3    | From dictionary (keys only)     | `T = tuple({key1: value1, key2: value2, ...})`      | Extracts keys as tuple               |
| 4    | From keyboard input             | `T = tuple(input("Enter tuple elements: "))`        | Input converted into tuple of chars  |

### `eval(input())` (Additional)

- Create tuple using `eval(input())` to preserve all the datatypes  
  `T = eval(input())`

## Accessing Tuples
#### Tuple Forward and Backward Indexing:

| Forward       | 0  | 1  | 2  | 3  | 4  |
|---------------|----|----|----|----|----|
| **Elementes** | **a**  | **e**  | **i**  | **o**  |**u** |
| Backward      | -5 | -4 | -3 | -2 | -1 |

- Store a reference at the each index instead of single character as in strings
- Each individual item stored somewhere in memory

#### Difference from List:
- Difference from List: Tuples are immutable

| Feature              | List                                | Tuple                               |
|----------------------|-------------------------------------|-------------------------------------|
| **Definition**       | Ordered collection of items         | Ordered collection of items         |
| **Mutability**       | Mutable (can be changed)            | Immutable (cannot be changed)       |
| **Syntax**           | Defined using square brackets `[]`  | Defined using parentheses `()`      |
| **Example**          | `my_list = [1, 2, 3]`              | `my_tuple = (1, 2, 3)`              |
| **Performance**      | Slower due to mutability overhead   | Faster due to immutability          |
| **Memory Usage**     | Requires more memory                | Requires less memory                |
| **Methods Available**| Many built-in methods (`append`, `extend`, `remove`, etc.) | Limited methods (`count`, `index`) |
| **Iteration**        | Slightly slower                    | Faster                              |
| **Use Case**         | Suitable for dynamic data           | Suitable for fixed/static data      |
| **Nested Structures**| Can contain lists, tuples, dicts    | Can contain lists, tuples, dicts    |
| **Hashability**      | Not hashable (cannot be used as dict keys) | Hashable if all elements are immutable |

#### How to Make Tuples Mutable
- Since tuples are immutable, to modify them:
- num = ([1, 2, 3], [4, 5, 6])
- num[1] = [1, 2, 0]    ❌ Immutable - Type Error
- num[0][2] = 0         ✓ Mutable - Changes inner list

- print(num)  # O/P: ([1, 2, 0], [4, 5, 6])

#### Traversing a Tuples

```python
# Example: 
T = ('P',"y",'t', "h', o, n")
print(T)  # O/P: ('P', 'y', 't', "h', o, n")
for a in T:
    print(a)
# O/P: 
# ['P']
# ['y']
# ['t']
# ["h', o, n"]

T2 = ('P', 'Y', 'T', 'H', 'O', 'N')
for b in T2:
    print(b, end=" ")  
# Output: P Y T H O N

length = len(T)
for index in range(length):
    print('At indexes', index, 'and', (index-length), 'element: ', T[index])
# O/P:
# At indexes 0 and -4 element:  P
# At indexes 1 and -3 element:  y
# At indexes 2 and -2 element:  t
# At indexes 3 and -1 element:  h', o, n
```

### Tuple Operations
#### Joining, Slicing & Replicating the Tuples:

#### Slicing:
- Giving Upper limit beyond the size of the tuple, it is automatically falling in range
- Giving Lower limit beyond much lower, it is automatically falling in range

| Operation                 | Syntax / Example        | Description / Notes                                                                                                                                                                  |
|---------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Concatenation or Join (+) | `T1 + T2`               | Concatenates tuples. ⚠️ Both operands must be tuples. <br> - `tuple + number` → ❌ Error <br> - `tuple + list` → ❌ Error <br> - `T1 + (3)` → ❌ Error <br> - `T1 + (3,)` → ✓ Valid |
| Replicate (*)             | `T * n`                 | Repeats the tuple elements `n` times.                                                                                                                                                |
| Slicing                   | `T[start:stop]`         | Extracts sub-parts of a tuple from `start` index up to `stop-1`.                                                                                                                     |
| Slicing with step         | `T[start:stop:step]`    | Extracts elements with a step interval. `Example: `T[0:10:2]` → selects every 2nd element.`                                                                                          |

[Examples: Join, Replicate & Slicing](3.join-replicate-slicing.py)

#### Comparing Tuples
- Compare two tuples without having to write code with loops for it.
- Comparison operators: `<`, `>`, `==` etc...

```python
a = (1, 2, 3)
b = (1, 2, 3)
c = (1, '2','3')

print(a == b)  # O/P: True
print(a == c)  # O/P: False
print(a > c )  # O/P: False

d = (1.0, 2.0, 3.0)
print(a == d)  # O/P: True
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

#### Tuple Built-in Functions & Methods

| Function   | Syntax                  | Description                                  |
|------------|-------------------------|----------------------------------------------|
| len()      | `len(<tuple>)`          | Returns the length of the tuple              |
| max()      | `max(<tuple>)`          | Returns the maximum element                  |
| min()      | `min(<tuple>)`          | Returns the minimum element                  |
| sum()      | `sum(<tuple>)`          | Returns the sum of all elements              |
| index()    | `<tuple>.index(<item>)` | Returns the index of the specified element   |
| count()    | `<tuple>.count(<item>)` | Returns the count of an item                 |
| Membership | `in`, `not in`          | Checks if an element exists in the tuple     |

[Examples: Functions and Methods](5.functions-methods.py)

#### sorted() - Returns a sorted list.
`Syntax: sorted(<iterable>)`
#### tuple() - Constructor method - used to create different types of values.
```python# Syntax: tuple(<seq>)
t = tuple("abc")  
# O/P: ('a', 'b', 'c')
```

#### `tuple()` - Create tuple from List 
```python
t = tuple([1, 2, 3])  
# O/P: (1, 2, 3)
```

#### `tuple()` - Create tuple from Dictionary
```python
t = tuple({'1': '11', 2: '2'})  
# Output: ('1', 2)
```

#### Deleting Tuples
```python
# Syntax: del <tuplename>
t1 = (5, 7, 9)
del t1
print(t1)  # Output: NameError - not defined
```

### Indirectly Modifying Tuples
#### 1) Using Tuple Unpacking, Modify 
```python
tpl = (11, 33, 66, 99)   # Input or Original value
print(tpl)               # O/P: (11, 33, 66, 99)
a, b, c, d = tpl         # Unpack
c = 77                   # Modify value in third element
tpl = (a, b, c, d)       # Assign values to original
print(tpl)               # O/P: (11, 33, 77, 99)
```

#### 2) Convert List, Modify and Using Tuple Constructor function:
```python
tpl = ("Kiryu", 35000, 17, "Admin") # Input or Original value
print (tpl)                         # O/P: ('Kiryu', 35000, 17, 'Admin')
lst = list(tpl)                     # Convert into List
lst[1] = 45000                      # Modify value in second element
tpl = tuple(lst)                    # Assign values to original
print(tpl)                          # O/P: ('Kiryu', 45000, 17, 'Admin')
```