''' Inheritance in Python
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (child) to inherit properties and methods from another class (parent). 

Key Concepts
Parent (Base/Super) Class: The class being inherited from.

Child (Derived/Sub) Class: The class that inherits the parent class.

Syntax:
class ParentClass:
    # Parent class body
    pass

class ChildClass(ParentClass):
    # Child class body
    pass
    
When we do this we are inheriting all the methods and parameters included in the parent class.
'''
# Basic example
class Mammals:
    def walking(self):
        print("Walking..")
class Humans(Mammals):
    
    def __init__(self, name="Unknown", age = 0):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hello party people, my name is {self.name} and I am {self.age}")
        
person1 = Humans()
person1.walking()


# Single inheritance: One child class inherits from one parent class.

class Animal:
    def speak(self):
        return "I am an animal."

class Dog(Animal):
    pass

d = Dog()
print(d.speak())  # Output: I am an animal.

# Multiple Inheritance: A child class inherits from multiple parent classes.

class A:
    def method_a(self):
        return "Method from A"

class B:
    def method_b(self):
        return "Method from B"

class C(A, B):
    pass

c = C()
print(c.method_a())  # Output: Method from A
print(c.method_b())  # Output: Method from B

# Multilevel Inheritance: A child class inherits from a parent class, which itself is a child of another class.

class Vehicle:
    def start(self):
        return "Vehicle started."

class Car(Vehicle):
    def drive(self):
        return "Car is driving."

class SportsCar(Car):
    def race(self):
        return "Sports car is racing."

sc = SportsCar()
print(sc.start())  # Output: Vehicle started. From Vehicle class
print(sc.drive())  # Output: Car is driving. From Car class.
print(sc.race())   # Output: Sports car is racing. From Sports car class

# Hierarchical Inheritance: Multiple child classes inherit from the same parent class.

class Animal:
    def speak(self):
        return "I am an animal."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

# Overriding Methods

# After a child class inherit from the parent class, we can override the methods we want with specific implementations
class Parent:
    def greet(self):
        return "Hello from Parent!"

class Child(Parent):
    def greet(self):
        return "Hello from Child!"

c = Child()
print(c.greet())  # Output: Hello from Child!

# After we override the method with our own implementation, what will we do if we want to access the method from the parent class
# To do that we can use the super() method which will help us access the methods in the parent class

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Initialize Parent attributes
        self.department = department

    def get_details(self):
        return super().get_details() + f", Department: {self.department}"

mgr = Manager("Alice", 80000, "HR")
print(mgr.get_details())  # Output: Name: Alice, Salary: 80000, Department: HR
