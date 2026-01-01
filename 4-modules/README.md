# MODULES

## What are Modules?
- **Strategy:** Dividing a bigger unit into smaller manageable units. Smaller handleable units are called **modules**.  
- **Python** → Preinstalled modules are called **Library**.  
- **Library** → Collection of modules that cater to specific types of needs or applications.  

**Example:**  
- NumPy → Scientific calculations (math, random, statistics modules).  
- PlayAudio → Used in different applications (mp3, fm, dvd, etc.).

### Advantages
- Reduces complexity to some degree  
- Creates well-defined, documented boundaries within the program  
- Can be reused in other programs  

------
#### Importing Modules

- Import Single Object
```python
# Syntax:
# from <module> import <objname>

# Example
from math import pi
print(pi)   # Output: 3.141592...
```
- Import Multiple Objects
```python
# Syntax:
# from <module> import <obj1>, <obj2>, [...]

# Example
from math import sqrt, pow, e
print(e)   # Output: 2.718281...
```

- Import All Objects
```python
# Syntax
# from <module> import *

# Example
from math import *
```

#### Math Module Functions
```python
math.sqrt(a*a + b*b + c*c)          # √(a²+b²+c²)
2 - 4*math.exp(2*x) + 4*x           # 2-4e²⁴+44
P + q/(math.pow(1+s, 4))            # P + q/(1+s²)
(math.cos(x)/math.tan(x)) + x       # (cos x/tan x)+x
math.fabs(math.exp(2)-x)            # |e²-x|
```
#### Random Module
```python
random.random()                     # Random float between 0 and 1
random.randrange(stop)              # Random integer up to stop
random.randrange(start, stop)       # Random integer in range
random.randrange(start, stop, step) # Random integer with step
```

#### Statistics Module
```python
import statistics

statistics.mean(seq)    # Average
statistics.median(seq)  # Middle value
statistics.mode(seq)    # Most frequent value
```

## Import Statement & Syntax
#### Import Entire Module
```python
import <module>
```

#### Import Selected Objects
```python
from <module> import <object>
```

#### Import Multiple Modules
```python
import module1, module2, ...
```
- Note: Import statement executes the code of the module file and then makes it available to your program.

#### Function Use (Dot Notation)
```python
<module-name>.<function-name>()

# Example
import tempConversion
tempConversion.to_Cen(98.6)   # Convert Fahrenheit to Celsius
tempConversion.to_far(80.0)   # Convert Celsius to Fahrenheit
```

#### Module Name Constant
```python
import time
print(time.__name__)   # Output: time
```

#### Alias Name
```python
# Syntax
import <module> as <aliasname>

# Example
import tempConversion as tc
tc.to_Cen(98.6)
```

#### Additional Topics
###### Random Module Example
```python
import random
print(random.random())                 # Output: 0.02235...
print(random.random() * (35-15) + 15)  # Random float between 15 and 35
print(random.randint(15, 35))          # Random integer between 15 and 35
```


