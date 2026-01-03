# LISTS
#### What is a List?
Lists are containers (mutable/modifiable) that are used to store a list of values of any type. Python lists are MUTABLE.
Key Characteristics:

- You can change the elements of a list in place
- It will create a fresh list when you make changes to any element
List is a type of sequence like strings and tuples but it differs in that strings & tuples are immutable

#### Creating & Accessing Lists
###### List Creation Syntax
| S.No | Syntax              | Description            |
|------|---------------------|------------------------|
| 1    | `[]`                | Create an empty list   |
| 2    | `[1, 2, 3]`         | Integer list           |
| 3    | `['a', 'b', 'c']`   | Character sequence     |
| 4    | `['a', 1, 3, 5, 'zero']` | Mixed data types list |

```python
# Examples
lstEmpty = []          # Empty list
lstValues = [0, 1, 2]  # List containing integers 0, 1, and 2

# Note:
# - Square brackets [ ] are used to define lists.
# - They appear at the beginning and end of the list definition.

# ✅ Access element in the list:
L1 = [1, 2, 3]         # Simple list
print(L1[0])           # Access element at index 0 → Output: 1
print(L1[1])           # Access element at index 1 → Output: 2
```

#### Nested List
```python
lstNested = [[3], [4], [5, 6], [7]]
# → Total 4 elements: 
print(lstNested[2][0]) 
# O/P: 5
print(lstNested[2][1])
# O/P 6
```

#### Input from keyboard
```python
lstInput = list(input("Enter list elements: "))
# Enter list elements: 23456789
print(lstInput)
# O/P: ['2', '3', '4', '5', '6', '7']
lstStr = list("hello")  
print(lstStr)
# O/P: ['h', 'e', 'l', 'l', 'o']  
```
- Note: The data type of all characters entered is (String) even though we entered digits.
To enter a list of integers using keyboard:
```python
list = eval(input("Enter list to be added: "))
# >> list you entered: [67, 78, 46, 23]
# >> This sometimes doesn't work in Python Shell
```

#### Accessing Lists (Index)
list = ['a', 'e', 'i', 'o', 'u']

| Forward Index  | 0    |  1  |  2  |  3  |  4  |
|----------------|------|-----|-----|-----|-----|
| Elements       | 'a'  | 'e' | 'i' | 'o' | 'u' |
| Backward Index | -5   | -4  | -3  | -2  | -1  |

```python
### Accessing List Elements
lst = [17, True, 'Good']

|-----------|----------------------|-----------------------------------|
| Index     | Element              | Notes / Operations                |
|-----------|----------------------|-----------------------------------|
| 0  (-3)   | lst[0] or lst[-3]    | Accessed directly                 |
|-----------|---------------|------------------------------------------|
  
# Refers to **Memory address of elements** supports **Concatenation (+)** and **Replication (*)**
print(lst[0])       # O/P: 17  at 0 index
print(lst[-5])      # O/P: Invalid index: Python will raise → Index Error
# (Ex: lst[3]) or lst[-6] → list index out of range
```
#### Difference between List vs String:
- List: Mutable; 
- String: Immutable

#### Traversing Lists
- Using Loop
```python
L1 = ['P', 'Y', 'T', 'H']
# Process each item here
for a in L1:
    print(a)
# Output: 
# P
# Y
# T
# H
# use more value to iterate
```

#### List Built-in Functions & Methods

| S.No | Function | Syntax                           | Description                                      |
|------|----------|----------------------------------|--------------------------------------------------|
| 1    | len()    | `len(<list>)`                    | Returns the length of the list                   |
| 2    | list()   | `list(<sequence>)`               | Converts a sequence (string, tuple, dict keys) into a list |
| 3    | index()  | `<list>.index(<item>)`           | Returns the index of the specified item          |
| 4    | append() | `<list>.append(<item>)`          | Adds an item to the end of the list              |
| 5    | extend() | `<list>.extend(<list>)`          | Adds multiple elements from another list         |
| 6    | insert() | `<list>.insert(<index>, <item>)` | Inserts an item at the given position          |
| 7    | pop()    | `<list>.pop(<index>)`            | Removes and returns the item at the given index  |
| 8    | remove() | `<list>.remove(<value>)`         | Removes the first occurrence of the specified value |
| 9    | clear()  | `<list>.clear()`                 | Removes all items from the list                  |
| 10   | count()  | `<list>.count(<item>)`           | Returns the count of the specified item          |
| 11   | reverse()| `<list>.reverse()`               | Reverses the items of the list                   |

#### sort()
Sorts an item, default increasing.
```python
# Syntax: List.sort([<reverse=False/True>])
# Example: List.sort(reverse=True)

val = [17, 24, 15, 30]
print(val.sort()) # None
print(val)   # Output: [15, 17, 24, 30]
val.sort(reverse=True)
print(val)   # Output: [30, 24, 17, 15]

# ⚠️ No return value
```

#### sorted()
- Takes the name of list as an argument and return new list.
###### Syntax: `sorted(<iterable-seq>, [reverse=False])`
```python
val = [17,24,15,30]
sval = sorted(val) 
print(sval)                       # O/P: [15, 17, 24, 30]
print(sorted(val, reverse=True))  # O/P: [30, 24, 17, 15]

# ⚠️ It return a new list
# → It creates new list with sorted version
# → It takes any iterable sequence type to list/tuples/dictionary
# → It returns newly created sorted list/tuples/dictionary
# → It doesn't change passed sequence
```

##### Difference Between `sort()` and `sorted()` in Python Lists

| Feature                | `list.sort()`                                         | `sorted(list)`                                                                       |
|-------------------------|------------------------------------------------------|--------------------------------------------------------------------------------------|
| **Type**               | Method of list object                                 | Built-in function                                                                    |
| **Return Value**       | Returns `None` (modifies list in place)               | Returns a **new sorted list**                                                        |
| **Original List**      | Gets changed (in-place sorting)                       | Remains unchanged                                                                    |
| **Usage**              | `numbers.sort()`                                      | `sorted(numbers)`                                                                    |
| **Flexibility**        | Works only on lists                                   | Works on any iterable (list, tuple, set, dict keys, etc.)                            |
| **Performance**        | Slightly faster (no new list created)                 | Slightly slower (creates a new list)                                                 |
| **Example**            | `a = [3,1,2]`<br>`a.sort()`<br>`print(a)` → `[1,2,3]` | `a = [3,1,2]`<br>`b = sorted(a)`<br>`print(a)` → `[3,1,2]`<br>`print(b)` → `[1,2,3]` |


#### 3 Ways to copy of a list:
- Using assignment operator to Copy of a List
- list()
- copy()
- Storing all elements of list using list slice with copy

#### Using `assignment operator` and `list() method` to Copy of a List
```python
a = [1, 2, 3]

# Use assignment operation
b = a  # (same ref)  [1][2][3] → lst1
       #             ↑↑↑  lst2
# Create an alias

a[1] = 5
a  # Op: [1, 5, 3]
b  # Op: [1, 5, 3]

b = list(a)
a  # [1][2][3] → lst 1
b  # [1][2][3] → lst 2
```

#### `copy()` - Method
```python
# True independent copy of list. copy() method → Creating the true copy of a list.
la = [11, 12, 13]
lb = la.copy()
la  # Output: [11, 12, 13]
lb  # Output: [11, 12, 13]
lb[0] += 10  # VALID It : [21, 12, 13]
la  # Output: [11, 12, 13]
```

##### Storing all elements of list using list `slice` with copy
```python
# Syntax: lstcopy = List[:] - Assignment operator`
# Ex: 
la = [11, 12, 13]  
lstcpy = la[:]  
print(lstcpy)      # Output: [11, 12, 13]`
```

#### Python  `copy()`, `slice` and `list()` Examples

| **Expression**            | **Code Example**                                                                       | **Output**                                         | **Explanation**                                                        |
|---------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------|------------------------------------------------------------------------|
| Simple copy               | `a = [1, 2, 3]`<br>`b = a.copy()`<br>`print(b)`                                        | `[1, 2, 3]`                                        | Creates a new list `b` with the same elements as `a`.                  |
| Modify copy only          | `a = [1, 2, 3]`<br>`b = a.copy()`<br>`b[0] = 99`<br>`print(a)`<br>`print(b)`           | `a → [1, 2, 3]`<br>`b → [99, 2, 3]`                | Changing `b` does not affect `a`.                                      |
| Nested list (shallow)     | `a = [[1, 2], [3, 4]]`<br>`b = a.copy()`<br>`b[0][0] = 99`<br>`print(a)`<br>`print(b)` | `a → [[99, 2], [3, 4]]`<br>`b → [[99, 2], [3, 4]]` | Shallow copy: inner lists are still shared.                            |
| Compare with assignment   | `a = [1, 2, 3]`<br>`b = a`<br>`b[0] = 99`<br>`print(a)`                                | `[99, 2, 3]`                                       | Assignment creates an alias, not a copy — both refer to the same list. |
| Alternative copy (slice)  | `a = [10, 20, 30]`<br>`b = a[:]`<br>`print(b)`                                         | `[10, 20, 30]`                                     | Slicing also creates a shallow copy of the list.                       |
| Alternative copy (list()) | `a = [5, 6, 7]`<br>`b = list(a)`<br>`print(b)`                                         | `[5, 6, 7]`                                        | Using `list()` constructor makes a shallow copy.                       |


#### List Operations

#### Comparing Lists
```python
(L1), (L2) = [1, 2, 3], [1, 2, 3]
print(L1 == L2)  # O/P: True
print(L1[1] == L2[1])  # O/P: False
print(L1 < L2)   # O/P: False
print(L1 < L2[1])   # O/P:Type Error
# ERROR: L1[1] → (integer), L2[1] is (List)
#        L1 + 2 (not)  Both not comparable
#        L1 + "abc" ✗  Both must be same type
```

#### List Operator: renamed list

- Individualized list added or exact as combined
- Joining List: (+)
- Concatenated list.
```python
lst1 = [1, 3, 5]
lst2 = [6, 7, 8]
lst1 + lst2  # Output: [1, 3, 5, 6, 7, 8]

# Both the operands must be same type
# Otherwise Type Error:
# (Ex) str[1] += 2  # Error (Int object in at iterable)
#      lst1 + "abc"  # No Error  Output: [1, 3, 5, 'a', 'b', 'c']

lst3 = [1, 0, 2, 0, 5, 0]
lst3 == lst1  # O/P: True
# ⚠️ Python ignores data types only compares values
Increase Error: list index out of range

lst3[6] → Increase Error: list index out of range
```

#### Repeating/Replicating List: (*)
```python
lst1 = [1, 3, 5]
lst1 * 3  # Output: [1, 3, 5, 1, 3, 5, 1, 3, 5]
# (*) → operator specifies to replicate with specified no. of times
```

#### Slicing Lists
- Normal Index
- Outside the list raises IndexError, exec L3
###### Slice
- Slice index are treated as boundaries instead:
```python
# Syntax: seq = L[start:stop]
# L[:] - slice index are treated as boundaries

# Example: 
lst = [10, 12, 14, 20, 22, 24, 30, 32, 34]

seq = lst[3:-3]                        # Output: [20, 22, 24]
seq[7] = 28                            # Output: [20, 28, 24]

print(lst[3:30])                       # ⬇️ No error! exceed up.lmt 
print(lst[-15:7])                      # exceed lower lmt
print(lst[6:10])                       # Output: [3]
print(lst[10:20])  #Op: [5] → (Empty)  # ⚠️ Both limit exceed 
```

#### Slices are treated as boundaries in sublist:
###### STEP:
```python
# Syntax: seq = L[start:stop:step]

# Ex: 
    lstStep = [10, 12, 14, 20, 22, 24, 30, 32, 34]
    lstStep[0:10:2]  # Step
    # O/P: [10, 14, 22, 30, 34]
    
    lstStep[2:10:3]
    # O/P: [14, 24, 34]  # No start, stop
    lstStep[::3]    # → (entire lst here - every 3rd element)
    lstStep[::‐1]
    # O/P: [34, 32, 30, 24, 22, 20, 14, 12, 10]
```

#### Accessing Through Indexes in Loop
```python
length = len(L1)
for a in range(length):
    print("At index", a, "and", (a-length), elem, L[a])

