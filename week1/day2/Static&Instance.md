# Static and Instance Members

In Object-Oriented Programming (OOP), classes can have both static and instance members.


## Static Members (class members)

**Static Members** are attributes and methods that belong to the class itself rather than to any particular instance of the class. They are shared among all instances of the class.

### Definition and Use Cases

- **Definition:** Static members are variables or methods that are not tied to a specific instance of the class. They are accessed using the class name rather than an object instance.

- **Use Cases:**
  - **Shared Data:** Useful for data that should be consistent across all instances, such as configuration settings or counters.
  - **Utility Methods:** Ideal for methods that do not need access to instance-specific data but provide general functionality applicable to the class as a whole.


## Instance Members

**Instance Members** are attributes and methods that are associated with a specific instance of the class. Each object of the class has its own set of instance members.

### Definition and Scope

- **Definition:** Instance members include both variables and methods that are specific to an object created from the class. They define the state and behavior of individual objects.

- **Scope:** Instance members are scoped to the specific object they belong to. They are initialized in the class's constructor (`__init__` method in Python) and are accessible using the object instance.


### How Instance Members are Used and Accessed

- **Initialization:** Typically, instance members are initialized in the constructor method of the class.
- **Usage:** Instance members are used to store and manage data that is unique to each object. They are accessed through the object instance using dot notation.

---

## Difference Between Static and Instance Members

- **Static Members:**
  - Belong to the class itself and can't modify data or accept any instance or class vars .
  - Shared across all instances of the class.
  - Accessed via the class name.

- **Instance Members:**
  - Belong to individual instances of the class.
  - Unique to each object instance.
  - Accessed through object instances.

## Examples of Static and Instance Members
```python
class TestClsSelf:
    clsr = "i'm a var for cls "
    
    def __init__(self):
        self.var = 'self var'

    @staticmethod
    def static_meth():
        return "Static method can't access instance or class variables"

    @classmethod
    def cls_meth(cls):
        return cls.var
```

### Static Members Example

- **Definition:** A static variable (class var) `counter` that tracks the number of instances created.
- **Usage:** Accessed via the class name to keep track of the total instances.

```python
"""
this is simple to show the use of static var to count the number of  but i can even add timer to each one if i had database to track every time request to see if there high traffic or something 
"""
class TrackedClass:
    counter=0 # static var (class var)
    def __init__(self,name):
        self.name = name
        TrackedClass.counter += 1 # every time instance created add one 
        
```
### Instance Members Example

- **Definition:** An instance variable `name` that stores the name of an individual object.
- **Usage:** Accessed through the object instance to retrieve or modify the specific object's name.

## Operator Overloading

**Operator Overloading** allows you to define custom behavior for operators (such as `+`, `-`, `*`, etc.) when applied to instances of user-defined classes.

### Concept and Implementation

- **Concept:** Operator overloading enables you to specify how standard operators should behave when used with objects of your class. This can make the objects interact in a more intuitive and natural way.

- **Implementation:** In Python, this is done by defining special methods in the class, which have double underscores before and after their names (e.g., `__add__`, `__sub__`).

### Examples of Operator Overloading in Various Languages
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

```python
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __repr__(self):
        return f"{self.real} + {self.imag}i"
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, 4)
c3 = c1 + c2  # Calls __add__
print(c3)     # Output: 4 + 6i
```
- **Python:** Overloading the `+` operator to add two custom objects, such as `Vector` or `ComplexNumber`.

Understanding these concepts helps in designing classes that are both flexible and intuitive, allowing for more natural interactions with class instances and operators.

# Class Variables in Python

## Instance Variables (`self.var`)
- **Use When**: You need to store data that is unique to each instance of the class.
- **Example**: Attributes like a user’s name or age in a `User` class.

## Class (Static) Variables (`Class.var`)
- **Use When**: You need to store data that is shared among all instances of the class.
- **Example**: A count of all instances created in a class, or a configuration setting applicable to all instances.

## Private Variables (`__var`)
- **Use When**: You want to encapsulate data and restrict access from outside the class, ensuring that it is accessed only through class methods.
- **Example**: Internal state that should not be modified directly, like sensitive data or implementation details.

## Protected Variables (`_var`)
- **Use When**: You want to signal that a variable is intended for internal use within the class and its subclasses, though access is not strictly enforced.
- **Example**: Variables that are intended to be used by subclasses or within the class, but not by external code.
