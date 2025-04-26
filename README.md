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

# Python Indexing:

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

# Built-in Functions & Methods:

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

# Programming Paradigms

## Procedure-Oriented Programming (POP)

- **Definition**:  
  Procedure-Oriented Programming focuses on writing a sequence of instructions (procedures/functions) to accomplish a task.  
  The main focus is on **functions and procedures**, not on data.

- **Problems in POP**:
  1. **Understandability**:  
     - Programs can become **large and complex**, making it difficult to understand, maintain, and modify.
  2. **Security**:  
     - Variables are often **globally declared**, making data accessible throughout the program and less secure.
  3. **Code Reusability**:  
     - Difficult to reuse code because procedures are tightly connected to each other.

- **Example** (in C):

    ```c
    int a, b;
    void add() {
        printf("%d", a + b);
    }
    int main() {
        a = 5; b = 10;
        add();
        return 0;
    }
    ```

- **Solution**:  
  To solve these issues, **Object-Oriented Programming (OOP)** was introduced.

---

## Object-Oriented Programming (OOP)

- **Definition**:  
  Object-Oriented Programming organizes code using **classes** and **objects**, focusing on real-world entities.  
  It makes programs easier to manage, secure, and reusable.

- **Real-World Example**:  
  Think of a **Car**:  
  - **Attributes**: color, brand, model (data)  
  - **Behaviors**: drive, brake, horn (methods)

---

### Features of OOP

1. **Class**:
   - A **class** is a **blueprint** or **template** that defines the structure and behavior (data + methods) of objects.
   - It is an **imaginary concept** — it does not occupy memory by itself.
   - **Example**:  
     ```python
     class Car:
         pass
     ```

2. **Object**:
   - An **object** is an **instance** of a class.
   - It is a **real-world entity** that occupies memory when created.
   - **Example**:  
     ```python
     car1 = Car()
     ```

3. **Encapsulation**:
   - **Definition**:  
     Encapsulation means **binding data and methods together** inside a class and **hiding** the internal details from the outside world.
   - **Purpose**:  
     It protects the integrity of data and restricts unauthorized access.

4. **Polymorphism**:
   - **Definition**:  
     Polymorphism means the **same function name** can behave **differently** based on different inputs or classes.
   - **Purpose**:  
     It provides flexibility and allows code to be more generic.

5. **Inheritance**:
   - **Definition**:  
     Inheritance allows a **child class** to **acquire** the properties and methods of a **parent class**.
   - **Purpose**:  
     It promotes code reuse and establishes a relationship between classes.

6. **Abstraction**:
   - **Definition**:  
     Abstraction means **showing only the essential features** and **hiding** the unnecessary details from the user.
   - **Purpose**:  
     It simplifies complexity by focusing only on what is important.
   - **Real-World Example**:  
     When driving a car, you only need to know how to use the steering wheel, brakes, and accelerator — you don't need to know how the engine works internally.

---

- **Example** (in Python):

    ```python
    class Car:
        def __init__(self, brand, color):
            self.brand = brand
            self.color = color

        def drive(self):
            print(f"The {self.color} {self.brand} car is driving.")

    car1 = Car("Toyota", "Red")
    car1.drive()
    ```

---

# Modules and Packages

- **Module**:
  - A **module** is a single `.py` file containing Python definitions and statements (functions, classes, etc.).
  - It helps organize related code into a logical file.
  
- **Package**:
  - A **package** is a **directory** that contains multiple modules and an `__init__.py` file.
  - It helps organize larger projects and **avoids naming conflicts**.

- **Example Structure**:
  ```
  mypackage/
      __init__.py
      module1.py
      module2.py
  ```

---

# File Accessing in Python

- **Definition**:  
  Python provides the `open()` function to **open and manipulate files** (read, write, append, etc.).

- **Syntax**:

  ```python
  file_object = open(filename, mode, buffering)
  ```

- **Parameters**:
  - **filename**: Name (and path) of the file.
  - **mode**: How the file should be opened (e.g., read, write).
  - **buffering**:
    - `-1` (default): System default buffering.
    - `0`: No buffering (for binary mode).
    - `1`: Line buffering.
    - Positive integer: Buffer size in bytes.

- **Modes**:
  | Mode | Meaning |
  |:-----|:--------|
  | `r`  | Read (default) |
  | `w`  | Write (overwrites file) |
  | `a`  | Append (adds data to the end) |
  | `b`  | Binary mode (e.g., images) |
  | `r+` | Read and Write |

- **Example**:

  ```python
  # Opening a file for reading
  file = open("example.txt", "r")

  # Opening a file for writing
  file = open("example.txt", "w")

  # Opening a file in binary read mode
  file = open("example.jpg", "rb")

  file.close()
  ```
---

# Errors and Error Handling in Python

## What are Errors?

- **Errors** are problems that occur while running a program.
- If not handled, errors can cause the program to **crash**.

---

## Types of Errors

1. **Syntax Errors**:
   - Errors due to wrong Python syntax.
   - Program won't even start running until the syntax is corrected.
   - **Example**:
     ```python
     if True
         print("Hello")
     ```
     (Missing `:` after `if True`)

2. **Runtime Errors**:
   - Errors that occur **while the program is running**.
   - Syntax is correct, but some operation fails during execution.
   - **Example**:
     ```python
     print(10 / 0)  # Division by zero error
     ```

3. **Logical Errors**:
   - The program runs without crashing but **produces wrong results**.
   - These are **hard to detect** because the code looks fine.
   - **Example**:
     ```python
     # Intention was to add numbers, but code multiplies
     def add(a, b):
         return a * b
     print(add(2, 3))  # Wrong output: 6 instead of 5
     ```

---

## Error Handling in Python

- To **handle** errors and prevent program crashes, Python provides the **try-except** block.

---

### Syntax:

```python
try:
    # Code that may cause an error
except ErrorType:
    # Code to handle the error
```

- **try** block:  
  - Write the code that might throw an error.
- **except** block:  
  - Write how you want to **handle** the error.

---

## Example: Handling Division by Zero

```python
try:
    a = int(input("Enter a number: "))
    result = 10 / a
    print("Result:", result)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
```

**Output**:

```
Enter a number: 0
You cannot divide by zero!
```

or

```
Enter a number: abc
Invalid input! Please enter a number.
```

---

## Catching All Errors (Not Recommended)

- You can catch all errors using a general `except` block, but it's **better to catch specific errors**.

```python
try:
    # risky code
except Exception as e:
    print("Error occurred:", e)
```

---

# Best Practices for Error Handling

✅ Catch **specific exceptions** instead of using a generic `Exception`.  
✅ Keep the `try` block **as small as possible** (only risky code inside).  
✅ Provide **useful error messages** for better debugging.  
✅ Don't silently ignore errors — **log them** or **handle properly**.

---

## What is a Method?

- A **method** is a **function inside a class** that works with the object’s data.
- It is used to **define the behavior** of objects.

✅ **In short**:  
- Methods are **actions** that objects can perform.

---

### Syntax:

```python
class ClassName:
    def method_name(self, parameters):
        # method body
```

- `self` refers to the object calling the method.

---

### Example:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

# Create Object
dog1 = Dog("Buddy")
dog1.bark()  # Output: Buddy says Woof!
```

---

## Types of Methods

| 🔹 Type | 🔹 Purpose | 🔹 Syntax Example |
|:---|:---|:---|
| Instance Methods | Work with instance (object) attributes | `def method(self):` |
| Class Methods | Work with class itself (shared across all objects) | `@classmethod` |
| Static Methods | Utility methods, not dependent on instance or class | `@staticmethod` |

---

### Example of Class Method and Static Method:

```python
class School:
    school_name = "ABC High School"

    def __init__(self, student_name):
        self.student_name = student_name

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    @staticmethod
    def is_open(day):
        return day.lower() != "sunday"

# Using methods
student = School("John")
print(student.get_school_name())   # Class Method
print(School.is_open("Monday"))     # Static Method
```

---

✅ **Quick Summary**

| Concept | Meaning |
|:---|:---|
| Class | Blueprint for creating objects |
| Object | Instance (real) of a class |
| Method | Function inside a class working with objects |

---

# Constructor in Python

## What is a Constructor?

- A **constructor** is a special **method** in a class that **automatically runs** when an **object** is created.
- It is mainly used to **initialize** the object’s **attributes** (variables).

---

## Constructor Method: `__init__()`

- In Python, the constructor is called **`__init__()`**.
- It is **automatically called** when a new object is created from a class.

---

### Syntax:

```python
class ClassName:
    def __init__(self, parameters):
        # Initialize attributes
```

- `self`:  
  Refers to the **current object** being created.
- Other parameters are used to pass **initial values** for object attributes.

---

### Example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create object
p1 = Person("John", 25)
p1.display()
```

**Output**:
```
Name: John, Age: 25
```

---

## Key Points:

| 🔹 Feature | 🔹 Description |
|:---|:---|
| Name | Always `__init__()` |
| Purpose | Initialize object attributes |
| Called Automatically | When creating an object |
| `self` | Refers to the current instance of the class |

---

## Types of Constructors (Conceptually)

1. **Default Constructor**:
   - A constructor with **no parameters** (except `self`).
   - Initializes object with default values.
   - **Example**:
     ```python
     class Car:
         def __init__(self):
             self.brand = "Toyota"
     car1 = Car()
     print(car1.brand)
     ```

2. **Parameterized Constructor**:
   - A constructor that **accepts parameters** to initialize attributes with different values.
   - **Example**:
     ```python
     class Car:
         def __init__(self, brand):
             self.brand = brand
     car1 = Car("Tesla")
     print(car1.brand)
     ```

---

✅ **In simple words**:  
- A **constructor** is like **setting up everything** when you build a new house (object)!
- You don't have to call it manually — Python does it for you the moment you create an object.

---

# 📚 Access Modifiers in Python (Variables)

In Object-Oriented Programming (OOP), **access modifiers** decide:
> **Who can access a variable or method?**

✅ In Python, there are **3 types** (not 4 like Java/C++).

| Modifier | Syntax | Meaning |
|:---|:---|:---|
| Public | `variable_name` | Accessible from anywhere |
| Protected | `_variable_name` | Should not be accessed outside the class (but still possible) |
| Private | `__variable_name` | Name mangled → Not directly accessible outside |

---

# 🎯 Explanation with Example

```python
class Student:
    def __init__(self):
        self.name = "Karthik"         # public variable
        self._course = "DevOps"        # protected variable
        self.__password = "secret123"  # private variable

# Create object
s1 = Student()

# Public variable → accessible
print(s1.name)        # Output: Karthik

# Protected variable → accessible but not recommended
print(s1._course)     # Output: DevOps

# Private variable → NOT directly accessible
# print(s1.__password)  # ❌ Error: AttributeError

# But technically, you can access private by name mangling
print(s1._Student__password)  # Output: secret123
```

---

# 🔵 Quick Meaning of Each

| Type | Rule | Practical Meaning |
|:---|:---|:---|
| **Public** | No underscore | Free to access |
| **Protected** | Single underscore `_` | Meant for **internal use** inside class/subclasses |
| **Private** | Double underscore `__` | Meant to be **fully hidden**, needs special way to access |

---

# 📢 Important:

✅ Python **doesn't enforce strict access** like Java or C++.  
✅ It uses a **gentleman's agreement** → "We trust you to respect it."

Meaning:  
- **_protected** → "please don't touch it unless needed."
- **__private** → "really please don't touch unless you know what you are doing."

---

# 📢 Important Note:

- In Python **there is no "default" access modifier**.
- "Default" concept exists in **Java**, not Python.
- In Python, if you **don't use underscore**, it is **Public** by default.
