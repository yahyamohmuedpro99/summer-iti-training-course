# Embedded Objects

Embedded objects are instances of one class that are included as members within another class. This approach allows for the creation of complex structures and relationships between classes.

## Definition and Usage

- **Definition:** Embedded objects refer to instances of one class being used as attributes or members of another class. This helps in building classes with complex relationships by integrating objects of different types.

- **Usage:** Embedded objects are used to compose more complex objects from simpler ones, promoting modular design and code reusability. They are especially useful when a class needs to include or use functionality provided by another class.

## Differences Between Embedded Objects and Regular Objects

- **Embedded Objects:**
  - Exist as attributes within another class.
  - Serve to compose or enhance the functionality of the parent class.
  - Example: A `Car` class that includes an `Engine` object as an attribute.

- **Regular Objects:**
  - Stand alone and are not contained within other objects.
  - Used directly without necessarily being part of another class.
  - Example: An independent `Person` object.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def show_books(self):
        for book in self.books:
            print(book)

# Creating objects
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.show_books()
```
---

## Examples of Embedded Objects

### Embedded Objects Example

- **Definition:** A `Library` class that includes a list of `Book` objects.
- **Usage:** `Library` objects manage collections of `Book` objects, demonstrating the composition of complex types.

### Regular Objects Example

- **Definition:** A `Book` object on its own without any other class embedding it.
- **Usage:** Used independently or in a collection but not embedded within another class.

# Inheritance

Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a class to inherit properties and behaviors from another class.

## Basic Concepts

- **Definition:** Inheritance is a mechanism where a new class (subclass or derived class) inherits attributes and methods from an existing class (base class or parent class). It promotes code reuse and establishes a hierarchical relationship between classes.

- **Purpose:** The primary purpose of inheritance is to facilitate code reuse and to establish a natural hierarchy. It allows new classes to be built upon existing classes, reducing redundancy and enhancing maintainability.

## Types of Inheritance

- **Single Inheritance:**
  - **Definition:** A subclass inherits from a single superclass.
  - **Example:** A `Dog` class inheriting from an `Animal` class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Creating objects
dog = Dog("Buddy")
print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!
```

- **Multiple Inheritance:**
  - **Definition:** A subclass inherits from more than one superclass.
  - **Example:** A `FlyingFish` class inheriting from both `Fish` and `Bird` classes.
```python
class Fish:
    def swim(self):
        return "Swimming"

class Bird:
    def fly(self):
        return "Flying"

class FlyingFish(Fish, Bird):
    def characteristics(self):
        return f"{self.swim()} and {self.fly()}"

# Creating object
ff = FlyingFish()
print(ff.characteristics())  # Output: Swimming and Flying
```

- **Multilevel Inheritance:**
  - **Definition:** A subclass inherits from another subclass, forming a chain of inheritance.
  - **Example:** A `GrandChild` class inheriting from a `Child` class, which in turn inherits from a `Parent` class.


- **Hierarchical Inheritance:**
  - **Definition:** Multiple subclasses inherit from a single superclass.
  - **Example:** Both `Car` and `Bike` classes inheriting from a common `Vehicle` class.

```python
class Computer:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        return "Computer powered on."

class Laptop(Computer):
    def __init__(self, brand, battery_life):
        super().__init__(brand)
        self.battery_life = battery_life

    def info(self):
        return f"{self.brand} Laptop with {self.battery_life} hours battery life."

class Tablet(Computer):
    def __init__(self, brand, screen_size):
        super().__init__(brand)
        self.screen_size = screen_size

    def info(self):
        return f"{self.brand} Tablet with {self.screen_size}-inch screen."

# Creating objects
laptop = Laptop("Dell", 8)
tablet = Tablet("Apple", 10)

print(laptop.info())  # Output: Dell Laptop with 8 hours battery life.
print(tablet.info())  # Output: Apple Tablet with 10-inch screen.
```
