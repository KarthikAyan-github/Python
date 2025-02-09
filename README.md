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

### Summary:
- **Implicit type casting**: Happens automatically when there’s no risk of data loss. For example, converting an `int` to a `float`.
- **Explicit type casting**: Done manually to convert between types when needed. Can result in loss of precision (e.g., converting a float to an int).
- **TypeError**: Be cautious, as Python will raise a `TypeError` if the conversion is not possible (e.g., trying to convert a non-numeric string to an `int`).

---

### Python Indexing:

Indexing in Python refers to accessing the elements of an ordered collection (like a list, tuple, string, etc.) using an index. Python supports both positive and negative indexing.

---

### 1. **Positive Indexing**:
In positive indexing, the index starts from **0** for the first element and increases by one for each subsequent element.

#### Example:
```python
my_list = ['a', 'b', 'c', 'd']
print(my_list[0])  # Output: 'a'  (first element)
print(my_list[2])  # Output: 'c'  (third element)
```

### 2. **Negative Indexing**:
In negative indexing, the index starts from **-1** for the last element and decreases by one as you move towards the beginning of the collection.

#### Example:
```python
my_list = ['a', 'b', 'c', 'd']
print(my_list[-1])  # Output: 'd'  (last element)
print(my_list[-2])  # Output: 'c'  (second-to-last element)
```

### 3. **Indexing with Strings**:
Strings are sequences of characters, and you can use indexing to access individual characters in a string.

#### Example:
```python
my_string = "Hello"
print(my_string[1])  # Output: 'e'  (second character)
print(my_string[-2]) # Output: 'l'  (second-to-last character)
```

### 4. **Slicing**:
You can also use **slicing** with indexing to get a subset of elements from a sequence (list, string, tuple, etc.). The syntax is:  
`sequence[start:end:step]`

- `start` is the index where the slice begins (inclusive).
- `end` is the index where the slice ends (exclusive).
- `step` is the interval between indices (optional).

#### Example:
```python
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])  # Output: [20, 30, 40] (from index 1 to 3)
print(my_list[:3])   # Output: [10, 20, 30] (from start to index 2)
print(my_list[::2])  # Output: [10, 30, 50] (every second element)
```

---

### Supported Data Types for Indexing and Slicing:

1. **Lists**:
   Lists are **ordered** collections of items. You can index and slice lists.
   
   #### Example:
   ```python
   my_list = [1, 2, 3, 4]
   print(my_list[2])    # Output: 3
   print(my_list[1:3])  # Output: [2, 3]
   ```

2. **Tuples**:
   Tuples are similar to lists but **immutable**. You can index and slice tuples.
   
   #### Example:
   ```python
   my_tuple = (10, 20, 30, 40)
   print(my_tuple[1])   # Output: 20
   print(my_tuple[1:3]) # Output: (20, 30)
   ```

3. **Strings**:
   Strings are **immutable sequences of characters**. You can index and slice strings like lists or tuples.
   
   #### Example:
   ```python
   my_string = "Python"
   print(my_string[0])  # Output: 'P'
   print(my_string[1:4]) # Output: 'yth'
   ```

4. **Ranges**:
   Ranges are used to represent a sequence of numbers, and you can index them like lists or tuples.
   
   #### Example:
   ```python
   my_range = range(10)
   print(my_range[2])  # Output: 2
   print(list(my_range[1:5]))  # Output: [1, 2, 3, 4]
   ```

---

### Summary:
- **Indexing in Python is zero-based**: The first element of a collection has index `0`.
- **Negative indexing** helps you access elements from the end of the sequence.
- **Slicing** allows you to access a part of the sequence (e.g., sublist, substring).

| Data Type | Supports Indexing | Supports Slicing | Example of Indexing | Example of Slicing |
|-----------|-------------------|------------------|---------------------|--------------------|
| List      | Yes               | Yes              | `my_list[2]`        | `my_list[1:4]`     |
| Tuple     | Yes               | Yes              | `my_tuple[1]`       | `my_tuple[1:3]`    |
| String    | Yes               | Yes              | `my_string[0]`      | `my_string[2:5]`   |
| Range     | Yes               | Yes              | `my_range[3]`       | `list(my_range[1:5])` |

---

### Built-in Functions & Methods:

There are many **built-in functions** and **methods** that are used frequently across various types of applications. Below is a list of the most commonly used built-in methods and functions in Python, categorized by data type:

### 1. **Commonly Used Built-in Functions**:
These are functions provided by Python that are often used in everyday coding tasks.

- **`print()`**: Outputs a message to the console.
  ```python
  print("Hello, World!")
  ```

- **`len()`**: Returns the length (number of elements) of an object (e.g., string, list, tuple).
  ```python
  len("hello")  # Output: 5
  len([1, 2, 3])  # Output: 3
  ```

- **`type()`**: Returns the type of an object.
  ```python
  type(5)  # Output: <class 'int'>
  ```

- **`int()`, `float()`, `str()`**: Type casting functions that convert between data types.
  ```python
  int("42")  # Output: 42
  float("3.14")  # Output: 3.14
  str(100)  # Output: '100'
  ```

- **`sum()`**: Returns the sum of all elements in an iterable (e.g., list).
  ```python
  sum([1, 2, 3, 4])  # Output: 10
  ```

- **`min()`** and **`max()`**: Return the smallest and largest item from an iterable.
  ```python
  min([1, 2, 3, 4])  # Output: 1
  max([1, 2, 3, 4])  # Output: 4
  ```

- **`sorted()`**: Returns a sorted list of the specified iterable.
  ```python
  sorted([3, 1, 4, 2])  # Output: [1, 2, 3, 4]
  ```

- **`input()`**: Takes input from the user.
  ```python
  name = input("Enter your name: ")  # Waits for user input
  ```

- **`range()`**: Generates a sequence of numbers.
  ```python
  list(range(5))  # Output: [0, 1, 2, 3, 4]
  ```

- **`all()`** and **`any()`**: Returns `True` if all or any elements in an iterable are `True`, respectively.
  ```python
  all([True, True, False])  # Output: False
  any([True, False, False])  # Output: True
  ```

---

### 2. **String Methods**:
Strings are one of the most common data types in Python, and there are many useful string methods.

- **`upper()`**: Converts a string to uppercase.
  ```python
  "hello".upper()  # Output: 'HELLO'
  ```

- **`lower()`**: Converts a string to lowercase.
  ```python
  "HELLO".lower()  # Output: 'hello'
  ```

- **`strip()`**: Removes leading and trailing whitespaces.
  ```python
  "   hello  ".strip()  # Output: 'hello'
  ```

- **`replace()`**: Replaces a substring with another string.
  ```python
  "hello world".replace("world", "Python")  # Output: 'hello Python'
  ```

- **`split()`**: Splits a string into a list based on a delimiter.
  ```python
  "apple,banana,cherry".split(",")  # Output: ['apple', 'banana', 'cherry']
  ```

- **`join()`**: Joins a list of strings into a single string.
  ```python
  "-".join(["apple", "banana", "cherry"])  # Output: 'apple-banana-cherry'
  ```

---

### 3. **List Methods**:
Lists are widely used in Python, and their methods are essential for many real-world applications.

- **`append()`**: Adds an item to the end of the list.
  ```python
  my_list = [1, 2]
  my_list.append(3)  # Output: [1, 2, 3]
  ```

- **`extend()`**: Adds multiple items (from another iterable) to the list.
  ```python
  my_list = [1, 2]
  my_list.extend([3, 4])  # Output: [1, 2, 3, 4]
  ```

- **`insert()`**: Adds an item at a specific index.
  ```python
  my_list = [1, 2, 4]
  my_list.insert(2, 3)  # Output: [1, 2, 3, 4]
  ```

- **`remove()`**: Removes the first occurrence of a specified item.
  ```python
  my_list = [1, 2, 3]
  my_list.remove(2)  # Output: [1, 3]
  ```

- **`pop()`**: Removes and returns an item at a specified index (or the last item).
  ```python
  my_list = [1, 2, 3]
  my_list.pop()  # Output: 3, and list becomes [1, 2]
  ```

- **`sort()`**: Sorts the list in place.
  ```python
  my_list = [3, 1, 2]
  my_list.sort()  # Output: [1, 2, 3]
  ```

- **`reverse()`**: Reverses the elements of the list in place.
  ```python
  my_list = [1, 2, 3]
  my_list.reverse()  # Output: [3, 2, 1]
  ```

---

### 4. **Dictionary Methods**:
Dictionaries are key-value pairs, commonly used to represent structured data.

- **`get()`**: Retrieves the value for a given key, or returns a default value if the key doesn’t exist.
  ```python
  my_dict = {"name": "Alice", "age": 25}
  my_dict.get("name")  # Output: 'Alice'
  ```

- **`keys()`**: Returns a list of all the keys in the dictionary.
  ```python
  my_dict.keys()  # Output: dict_keys(['name', 'age'])
  ```

- **`values()`**: Returns a list of all the values in the dictionary.
  ```python
  my_dict.values()  # Output: dict_values(['Alice', 25])
  ```

- **`items()`**: Returns a list of key-value tuple pairs.
  ```python
  my_dict.items()  # Output: dict_items([('name', 'Alice'), ('age', 25)])
  ```

- **`update()`**: Updates the dictionary with elements from another dictionary.
  ```python
  my_dict.update({"city": "New York"})  # Adds key 'city' with value 'New York'
  ```

- **`pop()`**: Removes a specified key-value pair and returns the value.
  ```python
  my_dict.pop("age")  # Output: 25
  ```

---

### 5. **Set Methods**:
Sets are collections of unique items and are useful when you need to store non-duplicate data.

- **`add()`**: Adds an item to the set.
  ```python
  my_set = {1, 2, 3}
  my_set.add(4)  # Output: {1, 2, 3, 4}
  ```

- **`remove()`**: Removes an item from the set.
  ```python
  my_set.remove(3)  # Output: {1, 2, 4}
  ```

- **`union()`**: Combines two sets.
  ```python
  my_set = {1, 2}
  another_set = {3, 4}
  my_set.union(another_set)  # Output: {1, 2, 3, 4}
  ```

- **`intersection()`**: Returns the common elements between two sets.
  ```python
  my_set = {1, 2, 3}
  another_set = {2, 3, 4}
  my_set.intersection(another_set)  # Output: {2, 3}
  ```

---
