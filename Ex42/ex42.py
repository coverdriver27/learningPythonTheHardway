"""
Exercise 42: Is-A, Has-A, Objects, and Classes

"""

# Animal Is-A object or a parent class
class Animal(object):
    pass

# Dog Is-A Object that inherits traits from the Animal class
class Dog(Animal):

    def __init__(self, name):
        # Dog has a name
        self.name = name

# Cat Is-A Object that inherits traits from the Animal class
class Cat(Animal):

    def __init__(self, name):
        # Cat has a name
        self.name = name

# Person Is-A Object that is also a parent class
class Person(object):

    def __init__(self, name):
        # Person has a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# Employee is a object that inherits traits from the Parent class of class person
class Employee(Person):

    def __init__(self, name, salary):
        # Hmm what kind is this stange magic?
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary

# Fish is a object or a parent class
class Fish(object):
    pass

# Salmon is-a object that inherits traits from the parent class Fish
class Salmon(Fish):
    pass

# Halibut is-a object that inherits traits from the parent class Fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# santa is-a Cat
santa = Cat("Santa")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet called santa
mary.pet = santa

# frank is a employee that has a salary
frank = Employee("Frank", 120000)

# frank has a pet
frank.pet = rover

# flipper is a fish
flipper = Fish()

# crouse is a salmon
crouse = Salmon()

# harry is a halibut
harry = Halibut()

