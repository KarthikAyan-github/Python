# Python

This is for my python scripting practice.

-------------------------------------------------------------------------------------------------------------------

# Best Practices to write code

1. Date input - int, string, map, list ...
2. Data Transformation - List -> String (If user provide input in one type but the business logic   expects in other type)
3. Business Logic - logic to complete our task (Important)
4. Output

-------------------------------------------------------------------------------------------------------------------

# Data Types in Python

1. **int** (Integer): Represents any whole number, positive or negative, without decimals.  
   Example: `age = 23`

2. **float**: Represents any numerical value with a decimal point.  
   Example: `height = 5.5`

3. **str** (String): A sequence of characters, also referred to as a collection of characters or alpha-numeric values.  
   Example: `name = "Karthik"`, `address = "Areclia C 503"`

4. **list**: An ordered collection of items, which can be of any type, and allows duplicates. Lists are mutable, meaning you can modify them after creation.  
   Example: `my_list = [1, 2, 3, 4, 2]`

5. **tuple**: Similar to a list, but **immutable**. Once created, the contents of a tuple cannot be modified, added, or removed.  
   Example: `my_tuple = (1, 2, 3, 4, 4)`

6. **set**: An unordered collection of unique items. Sets automatically remove duplicates and are mutable.  
   Example: `my_set = {1, 2, 3, 4}` or `my_set = set([1, 2, 3, 4])`

7. **dict** (Dictionary): Stores values in **key-value pairs**, where each key is unique. Keys must be immutable (e.g., strings, numbers), and the values can be of any data type.  
   Example: `details = {"name": "Karthik", "age": 23, "height": 5.5}`

-----------------------------------------------------------------------------------------------------------------

# Python Type Casting: Data Transformation

Type casting is the process of converting one data type into another. In Python, you can explicitly cast data between types using built-in functions. 

Python provides **two types of type casting**:

1. **Implicit Type Casting** (also known as **automatic type conversion**): Python automatically converts a smaller data type to a larger one without user intervention.
2. **Explicit Type Casting** (also known as **manual type conversion**): The user explicitly converts one data type to another using casting functions.

---

### 1. **Implicit Type Casting**:
Python automatically converts lower data types (like integers) to higher data types (like floats) to avoid data loss.

#### Example:
```python
x = 10       # integer
y = 5.5      # float

result = x + y  # Python automatically converts 'x' to a float before performing the operation
print(result)   # Output: 15.5 (float)
```

---

### 2. **Explicit Type Casting**:
You can manually convert one data type to another using type casting functions.

#### Common Type Casting Functions:
- **`int()`**: Converts a value to an integer.
- **`float()`**: Converts a value to a float.
- **`str()`**: Converts a value to a string.
- **`list()`**: Converts an iterable (like a string, tuple, or set) into a list.
- **`tuple()`**: Converts an iterable into a tuple.
- **`set()`**: Converts an iterable into a set.

#### Examples:

1. **Convert a float to an integer:**
   ```python
   x = 3.14
   y = int(x)  # Casting float to integer (loses the decimal part)
   print(y)     # Output: 3
   ```

2. **Convert an integer to a string:**
   ```python
   x = 100
   y = str(x)  # Casting integer to string
   print(y)    # Output: "100"
   ```

3. **Convert a string to a float:**
   ```python
   x = "10.5"
   y = float(x)  # Casting string to float
   print(y)       # Output: 10.5
   ```

4. **Convert a tuple to a list:**
   ```python
   x = (1, 2, 3)
   y = list(x)  # Casting tuple to list
   print(y)     # Output: [1, 2, 3]
   ```

5. **Convert a string to a set:**
   ```python
   x = "hello"
   y = set(x)  # Casting string to set (duplicates removed)
   print(y)    # Output: {'h', 'e', 'l', 'o'}
   ```

---

### Notes:
- **Implicit type casting**: Happens automatically when there’s no risk of data loss. For example, converting an `int` to a `float`.
- **Explicit type casting**: Done manually to convert between types when needed. Can result in loss of precision (e.g., converting a float to an int).
- **TypeError**: Be cautious, as Python will raise a `TypeError` if the conversion is not possible (e.g., trying to convert a non-numeric string to an `int`).

---

This should give you a clear understanding of type casting in Python! Let me know if you need more details or examples.
