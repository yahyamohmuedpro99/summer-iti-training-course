# Polymorphism

Polymorphism is a core concept in Object-Oriented Programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables methods to be used in different ways depending on the object they are acting upon.

## Function Overloading

**Function Overloading** is a type of polymorphism that allows multiple methods to have the same name but different signatures (i.e., different parameter lists) within the same class. Although Python does not support traditional function overloading as some other languages do (like C++ or Java), you can achieve similar functionality using default arguments or variable-length arguments.

### Definition and Examples

- **Definition:** Function overloading allows multiple methods with the same name to coexist in a class, as long as their parameter lists differ. In Python, this is often achieved through default arguments or variable-length argument lists.

- **Example Using Default Arguments:**

    ```python
    class Printer:
        def print_message(self, msg=None, times=1):
            if msg is None:
                msg = "No message"
            for _ in range(times):
                print(msg)
    
    p = Printer()
    p.print_message()            # Calls with default arguments
    p.print_message("Hello")     # Calls with one argument
    p.print_message("Hello", 3)  # Calls with two arguments
    ```

  In this example, the `print_message` method can handle different numbers of arguments. If no arguments are provided, it prints a default message. If one argument is given, it prints that message once. If two arguments are provided, it prints the message the specified number of times.

## Operator Overloading

**Operator Overloading** allows you to define custom behavior for operators (like `+`, `-`, `*`, etc.) for user-defined classes. This makes it possible to use standard operators with objects of these classes in a way that is intuitive and natural.

### Definition and Use Cases

- **Definition:** Operator overloading allows you to specify what operators should do when applied to instances of a class. This makes it possible to use standard operators with objects in a manner that is consistent with their intended behavior.

- **Use Cases:**
  - Custom classes that need to support arithmetic operations.
  - Implementing comparisons or other operations that make sense for the class.

### Examples in Python

- **Example for Arithmetic Operator Overloading:**

    ```python
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)
        
        def __str__(self):
            return f"Vector({self.x}, {self.y})"
    
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    v3 = v1 + v2  # Calls __add__
    print(v3)      # Output: Vector(6, 8)
    ```

  In this example, the `+` operator is overloaded to add two `Vector` objects together. The `__add__` method defines how the addition should be performed.

- **Example for Comparison Operator Overloading:**

    ```python
    class Box:
        def __init__(self, length, width, height):
            self.length = length
            self.width = width
            self.height = height
        
        def __lt__(self, other):
            return self.volume() < other.volume()
        
        def volume(self):
            return self.length * self.width * self.height
        
        def __str__(self):
            return f"Box({self.length}, {self.width}, {self.height})"
    
    b1 = Box(2, 3, 4)
    b2 = Box(3, 4, 5)
    print(b1 < b2)  # Calls __lt__; Output: True
    ```

  In this example, the `<` operator is overloaded to compare the volumes of two `Box` objects. The `__lt__` method defines how the less-than comparison should be performed.

### Summary

Polymorphism in OOP allows methods and operators to be used flexibly and intuitively. **Function overloading** in Python is achieved using default or variable-length arguments, while **operator overloading** lets you define custom behaviors for operators in user-defined classes. These features enhance code readability and usability by allowing you to tailor operations for your specific classes.
