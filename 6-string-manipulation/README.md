## String Manipulations

- In Python Strings are characters enclosed in quotes of any types (`single, double or triple quotation marks`)
- Empty string has 0 characters
- Strings are immutable, 

#### Each characters has unique indexes
INDEX:
- Forward direction - Index begin with 0 and end with Length-1
- Backward direction - Index begin with -1 and end with -Length

#### Traversing String
- Using indexes, we can traverse a string character by character
- Using Loops
```python
# Example:
name = "Kiryu"
for ch in name:
    print(ch, '-', end= ' ')

# O/P: K - i - r - y - u -
```
#### String Indexing for "Kiryu"

| Forward Index  | 0   | 1   | 2   | 3   | 4   |
|----------------|-----|-----|-----|-----|-----|
| Input String   | K   | i   | r   | y   | u   |
| Backward Index | -5  | -4  | -3  | -2  | -1  |

[Example - String Reverse, display different form using LOOP and CONDITIONS](1.access.py)

#### String Operators

#### Basic Operators  (+ and *)
#### String Concatenation (+)
- Creates a new string by joining the two operand strings.
```python
#`Ex (String): 
"tea" + "pot"                   # O/P: 'teapot'
# Ex (Integer): 
1 + 8                           # O/P: 9
```

#### String Replicator (*)
-  String operand * tells the strings to be replicated
```python
#`Ex (String): 
3 * "go!"                         # O/P: 'go!go!go!'

"#" * 3                           # O/P: '###' 

# Ex (Integer): 
2 * 8                             # O/P: 16
"2" * "8"                         # O/P: Type Error
```

#### Membership Operators `in` and `not in`

#### Comparison Operators `<`, `<=`, `>`, `>=`, `==`, `!=`

#### String Slices

##### Python String Functions and Methods

| Category        | Functions / Methods                                                                 |
|-----------------|--------------------------------------------------------------------------------------|
| Built-in        | `len()`                                                                              |
| Case Conversion | `capitalize()`, `lower()`, `upper()`                                                 |
| Search          | `find()`, `index()`, `count()`                                                       |
| Validation      | `isalnum()`, `isalpha()`, `isdigit()`, `islower()`, `isupper()`, `isspace()`         |
| Whitespace      | `strip()`, `lstrip()`, `rstrip()`                                                    |
| Modification    | `replace()`                                                                          |
| Splitting/Joining| `split()`, `partition()`, `join()`                                                  |


