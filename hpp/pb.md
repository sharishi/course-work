# Basic Python Outline

## Basic Python syntax: Understanding variables, data types, loops, conditional
### Variables 
Variables in Python are named references to objects stored in the computer's memory.
Numeric: integers, floats, complex numbers.
### Data types
![text](data/pb1.png "Data Types")
### Loops
for/while
### Conditional statements 
if...elif...else
### Functions
```python
def func_name():
    ...
```
## Data structures: Lists, tuples, sets, dictionaries, and comprehensions

### Lists
Lists are ordered mutable collections of elements.
They can contain elements of different types and can be modified after creation.
1. Creating a list:
```python
my_list = [1, 2, 3, "hello", 3.14]
```
2. Accessing elements:
```python
first_element = my_list[0]   # 1
last_element = my_list[-1]    # 3.14
```
3. Modifying elements:
```python
my_list[1] = "world"
```
4. List methods:
```python
my_list.append(42)        # Adds an element to the end
my_list.remove("hello")   # Removes the first found element
length = len(my_list)     # Length of the list
```
### Tuples
Tuples are ordered immutable collections of elements.
They are used to store multiple values that should not change.

1. Creating a tuple:
```python
my_tuple = (1, 2, 3, "hello", 3.14)
```
2. Accessing elements:
```python
first_element = my_tuple[0]   # 1
```
Tuples do not support element modification.

### Sets
Sets are unordered collections of unique elements. 
They do not allow duplicate values.

1. Creating a set:
```python
my_set = {1, 2, 3, "hello"}
```
2. Set operations:

```python
my_set.add(4)                # Adds an element
my_set.remove(2)             # Removes an element (if it exists)
is_member = 3 in my_set      # Checks for the presence of an element
```
3. Set operations:
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2          # Union
intersection = set1 & set2   # Intersection
difference = set1 - set2     # Difference
```
