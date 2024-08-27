# Overriding

## Concept of Method Overriding

### Definition
Method overriding is a feature in object-oriented programming where a subclass provides a specific implementation of a method that is already defined in its superclass. This allows a subclass to modify or extend the behavior of methods inherited from the superclass.

### Examples
In method overriding, the method in the subclass must have the same name, return type, and parameters as the method in the superclass. The `super()` function is often used to call the method from the superclass if needed.

#### Example

```python
class Animal:
    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating objects
dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
```
## Differences Between Overriding and Overloading

- ### Method Overriding
            *Definition*: Subclass provides a new implementation of a method that is already defined in its superclass.

            *Purpose*: Allows subclasses to customize or extend inherited behaviors.
    
            *Example*: Dog class overriding speak() method from Animal class.

- ### Method Overloading
        *Definition*: Multiple methods with the same name but different parameters within the same class.

        *Purpose*: Provides different ways to perform an operation depending on the input.

        *Example*: In languages like Java or C++, you might have multiple print methods with different parameter lists. Python does not support method overloading natively but uses default arguments or variable-length argument lists instead.

    #### using default arguments
    ```python
    class Printer:
        def print(self, text=None, number=None):
            if text is not None:
                print(f"Text: {text}")
            if number is not None:
                print(f"Number: {number}")

    printer = Printer()
    printer.print("Hello")  # Output: Text: Hello
    printer.print(number=123)  # Output: Number: 123
    ```
    #### using variable-length 
    

    ```python
    class Example:
        def print_values(self, *args):
            for value in args:
                print(value)

    obj = Example()
    obj.print_values(1, 2, 3)  # Output: 1 2 3
    ```

    ```python
    class Example:
        def print_key_values(self, **kwargs):
            for key, value in kwargs.items():
                print(f"{key}: {value}")

    obj = Example()
    obj.print_key_values(name="Alice", age=30)  # Output: name: Alice  age: 30

    ```
    ##### how overloading look in other langs
    ```java
    class OverloadExample {
        // Method with one parameter
        void display(int a) {
            System.out.println("Argument: " + a);
        }

        // Overloaded method with two parameters
        void display(int a, int b) {
            System.out.println("Arguments: " + a + " and " + b);
        }

        public static void main(String[] args) {
            OverloadExample obj = new OverloadExample();
            obj.display(10);        // Calls the method with one parameter
            obj.display(10, 20);    // Calls the method with two parameters
        }
    }
    ```

## Abstract Classes and Interfaces

- ### Abstract Classes
        Definition:An abstract class is a class that cannot be instantiated on its own and is intended to be subclassed. It can contain abstract methods (methods without implementation) and concrete methods (methods with implementation).

        Use Cases 
            Design Frameworks: Define a blueprint for other classes to follow.
            
            Enforce Implementation: Ensure derived classes implement specific methods (must be implemented by any subclass).

            
- ### How to Define and Use Abstract Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def description(self):
        return "I am a shape"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating object
rectangle = Rectangle(5, 10)
print(rectangle.area())  # Output: 50
print(rectangle.description())  # Output: I am a shape
```

## Interfaces
- #### Definition 
            An interface is a contract that defines a set of methods that a class must implement. *Unlike abstract classes, interfaces do not provide any method implementations*.

- #### Purpose
            Define a Protocol: Specify a set of methods that implementing classes must provide.
        
            Multiple Inheritance: Provide a way to achieve multiple inheritance by allowing classes to implement multiple interfaces.

### How Interfaces Differ from Abstract Classes

    Abstract Classes: Can have both abstract methods and concrete methods (methods with implementations). Can also have attributes.

    Interfaces: Only define methods (without implementations) and constants. A class can implement multiple interfaces.

### How to Implement Interfaces
    Python does not have a dedicated interface keyword but uses abstract base classes to achieve similar functionality.

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Document(Drawable, Printable):
    def draw(self):
        return "Drawing document"

    def print(self):
        return "Printing document"

# Creating object
doc = Document()
print(doc.draw())  # Output: Drawing document
print(doc.print())  # Output: Printing document
```


