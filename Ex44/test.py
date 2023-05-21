class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal speaks.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("The dog barks.")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.pet = None

    def set_pet(self, pet):
        self.pet = pet

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        if self.pet:
            print(f"My pet {self.pet.name} is here with me.")


dog = Dog("Buddy", "Golden Retriever")
person = Person("Bruno", 30)
person.set_pet(dog)
person.greet()

dog = Dog("butters", "Golden terrier")
person = Person("Iceal", 300)
person.set_pet(dog)
person.greet()

"""
In this program, we have two classes: Animal and Dog. Dog inherits from Animal using the super() function to call the 
__init__() method of the parent class. Dog also overrides the speak() method of Animal to bark instead of speak.

We also have a Person class that has a pet attribute which can be set to an instance of Animal or one of its subclasses. 
The Person class has a greet() method that prints a greeting message along with the name of the pet, if there is one.

This program also uses composition to connect the Person and Dog classes. The Person class has a set_pet() method that 
takes an instance of Animal or one of its subclasses and sets it as the person's pet. In this case, we create an 
instance of Dog and set it as the person's pet using the set_pet() method.

When we run the program, it outputs:
"""
# Hello, my name is Alice and I am 30 years old.
# My pet Buddy is here with me.

"""
In this example, we see that inheritance is useful for creating a hierarchy of classes that share common attributes and 
methods, while allowing subclasses to override or extend them. On the other hand, composition is useful for creating 
relationships between objects of different classes, where one object contains or uses another object as a component. By 
combining these two concepts, we can create more complex programs that are flexible and reusable.
"""