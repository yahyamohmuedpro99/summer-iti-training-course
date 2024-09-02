# Encapsulation

## 1. Definition and Importance

- ### What is Encapsulation?

    Encapsulation is a fundamental concept in object-oriented programming that involves bundling data (attributes) and methods (functions) that operate on that data into a single unit called a class. This allows an object to control how its data is accessed and modified, which is crucial for maintaining integrity and abstraction.

- ### Importance of Encapsulation

   - *Data Hiding*: Encapsulation helps hide the internal state of an object from the outside world. This means that the internal representation of the object is shielded from direct access, reducing the risk of unintended interference and misuse.

    - *Control*: By controlling how data is accessed and modified, encapsulation allows the class to enforce rules and validations. This ensures that the object’s state remains consistent and valid.

    - *Flexibility and Maintainability*: Encapsulation makes it easier to change the internal implementation of a class without affecting external code that uses the class. This leads to more maintainable and adaptable code.

    - *Abstraction*: It helps in defining a clear and simple interface for interacting with an object while hiding the complex implementation details.

## 2. How to Encapsulate Data and Behavior Within a Class

- ## Defining a Class
    A class in OOP is a blueprint for creating objects. It encapsulates data attributes and methods into a single unit. in python:
    ```python
    class Example:
        def __init__(self):
            self.public_field = 1          # Public field
            self._protected_field = 2      # Protected field
            self.__private_field = 3       # Private field

        def public_method(self):
            pass                          # Public method

        def _protected_method(self):
            pass                          # Protected method

        def __private_method(self):
            pass                          # Private method```




## Members’ Modifiers

- ### Access Control: Public, Private, Protected

    - #### Public
            Definition: Members marked as public can be accessed from any other class or package.
            Usage: Public members are typically used for methods that need to be accessible from outside the class.

    - #### Private
            Definition: Members marked as private can only be accessed within the same class. They are not accessible from outside the class, not even by derived classes.
            Usage: Private members are used to encapsulate data and implementation details, providing access only through public methods (getters and setters).

    - #### Protected
            Definition: Members marked as protected can be accessed within the same package and by subclasses (derived classes) in other packages.
            Usage: Protected members are used when a class needs to allow subclasses to access or modify its data, but still wants to restrict access from other classes.

- ### How Modifiers Affect Data and Method Accessibility

    - #### Public Access
            Visibility: Public members are accessible from any code that has visibility of the class.
            Example: Methods like getName() and setName() in the Person class are public, allowing any other class to call these methods to access or modify the name attribute.
        
    - #### Private Access
            Visibility: Private members are only accessible within the class itself.
            Example: The name and age attributes in the Person class are private. They cannot be accessed directly from outside the class. Instead, access is controlled through public getter and setter methods.

    - #### Protected Access
            Visibility: Protected members are accessible within the same package and by subclasses, even if they are in different packages.
            Example: If you have a class Employee that extends Person, the Employee class can access protected methods and attributes of Person, but other classes that do not extend Person cannot.


```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        """Get the current balance."""
        return self.__balance

    def get_account_holder(self):
        """Get the name of the account holder."""
        return self.account_holder
```
