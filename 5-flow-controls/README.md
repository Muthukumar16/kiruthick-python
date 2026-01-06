## Flow controls
#### Introduction:
- Software program executes statements from <b>Start to End.</b>
- <b>Depending upon need</b> → Order of statements execution vary ex: conditional basis, repeat a set of statements etc.
- Python provides - Tools by providing statements to attain so. Such statements are called `Program control statements`
- Selection Statement - `if` and Iteration Statement - `for and while`

#### Types of statements
- Statements → The instruction given by computer to perform specific action, be it data movements.
- Ex: `Making decisions` or be it `repeating actions`.

1. Empty (Null) Statements: <br/>`pass` - statement, which does noting 
2. Simple Statement (Single statement): <br/>Single executable statement `name = input("Enter your name)`
3. Compound Statement:<br/>
`<compound statement header>:`<br/> &nbsp;&nbsp;&nbsp;&nbsp;`<indented body -> multiple simple and/or compound statements>`

### Statement Flow Control
#### Sequence
- The statements are being executed sequentially.
- When the final statement of program is executed, the program is done.

#### Selection
- Execution of statement depending upon a condition-test. 
- If a condition evaluates to `True`, a course of action is followed.
- Otherwise, another course of action if followed.

#### Repetition Iteration (Looping)

### The `If` Statements of Python
#### `if` Statement

#### `if - else` Statement

#### `if-elif-else` Statement

#### Nested `if` Statement

#### Storing Conditions

### Repetition of Tasks

#### `range()` Function

##### Different Ways to Print `range(0,5)` in Python

| **Method**                     | **Code Example**                               | **Output**                      | **Notes**                                            |
|--------------------------------|------------------------------------------------|---------------------------------|------------------------------------------------------|
| Convert to string with `str()` | `print(str(range(0,5)))`                       | `range(0, 5)`                   | Shows the range object itself, not the numbers.      |
| Convert to list                | `print(list(range(0,5)))`                      | `[0, 1, 2, 3, 4]`               | Displays the actual numbers as a list.               |
| Loop through range             | `for i in range(0,5): print(i)`                | `0`<br>`1`<br>`2`<br>`3`<br>`4` | Prints each number on a new line.                    |
| Join into string               | `print(" ".join(map(str, range(0,5))))`        | `0 1 2 3 4`                     | Clean string of numbers separated by spaces.         |
| Using unpacking                | `print(*range(0,5))`                           | `0 1 2 3 4`                     | Prints numbers separated by spaces automatically.    |
| List comprehension string      | `print([str(i) for i in range(0,5)])`          | `['0', '1', '2', '3', '4']`     | Shows numbers as strings inside a list.              |
| f-string with loop             | `print(", ".join(f"{i}" for i in range(0,5)))` | `0, 1, 2, 3, 4`                 | Flexible formatting with commas or other separators. |

#### Python `range()` Examples:

| **Expression**         | **Code Example**            | **Output**                       | **Explanation**                                       |
|------------------------|-----------------------------|----------------------------------|-------------------------------------------------------|
| `range(10)`            | `print(list(range(10)))`    | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` | Starts at 0 by default, goes up to 9 (stop-1).        |
| `range(5,10)`          | `print(list(range(5,10)))`  | `[5, 6, 7, 8, 9]`                | Starts at 5, stops before 10.                         |
| `range(3,7)`           | `print(list(range(3,7)))`   | `[3, 4, 5, 6]`                   | Starts at 3, stops before 7.                          |
| `range(5,15,5)`        | `print(list(range(5,15,5)))`| `[5, 10]`                        | Starts at 5, increments by 5, stops before 15.        |
| `range(9,3,-1)`        | `print(list(range(9,3,-1)))`| `[9, 8, 7, 6, 5, 4]`             | Counts backwards from 9 down to 4.                    |
| `range(10,1,2)`        | `print(list(range(10,1,2)))`| `[]`                             | Empty list because step is positive but start > stop. |


#### Operators `in` and `not in`

### Iteration/Looping Statements:

#### `for` Loop

#### `while` Loop

### Loop `else` Statements

#### Jump Statements - `break` and `continue`

#### `break` Statement

#### `continue` Statement

### Loop `else`

### Nested loops



