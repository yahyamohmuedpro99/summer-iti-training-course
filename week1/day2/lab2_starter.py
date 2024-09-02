
# class Displayer:
#     def __init__(self,itme=None):
#         self.itme = itme
#     def display(self):
#         if self.itme is None:
#             return "you didn't enter anything"
#         elif isinstance(self.itme,str):
#             return f"this is your string {self.itme}"
#         else:
#             return self.itme
    
# dis=Displayer("dfsasdf")
# print(dis.display())

from abc import ABC,abstractmethod
class Animal:
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    
    
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "meow!"
    def move(self):
        return "I'm a cat! and i'm running"

# Creating objects
dog = Dog("Buddy")
print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!
print(dog.move())  # Output: Woof!

cat = Cat("bosbos")
print(cat.name)  # Output: Buddy
print(cat.speak())  # Output: Woof!
print(cat.move())  # Output: Woof!