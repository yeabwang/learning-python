'''
Class
A class is a blueprint for creating objects. Objects are instances of classes and encapsulate data (attributes) and behavior (methods).

Constructor
A constructor in Python is a special method (__init__) used to initialize an object’s attributes when the object is created. It is automatically called when an object is instantiated.

Key Points:
The constructor method is named __init__.
It is optional. If not defined, Python provides a default constructor that does nothing.
Typically used to set up initial state (attributes) for the object.

Instance vs. Class Attributes
Instance attributes: Defined within the constructor using self (unique to each object).
Class attributes: Shared across all instances and defined outside the constructor.

'''


class Person:
    
    def __init__(self, name, age):
        self.nameOfPerson = name
        self.ageOfPerson = age
        
    def introduce(self):
        print(f"Hello everyone, my name is {self.nameOfPerson} and I am {self.ageOfPerson}")
    def birthday(self, is_birthday):
        if(is_birthday):
            print(f"Happy birthday {self.nameOfPerson}, you are now {self.ageOfPerson}")
            
            
def main():
    
    try:
        name = input("Whats your name: ")
        age = int(input("How old are you: "))
        is_your_birthday = bool(int(input("Today is your birthday? 1 for True and 0 for False: ")))

        person1 = Person(name,age)
        person1.introduce()
        person1.birthday(is_your_birthday)
        person1.idNumber = 32123
        
        print(f"Your ID number is {person1.idNumber}")
    
    except Exception as e:
        print(e)
main()