"""
Exercise 42: Is-A, Has-A, Objects, and Classes

"""

#
class Animal(object):
    pass

#
class Dog(Animal):

    def __init__(self, name):
        #
        self.name = name

#
class Cat(Animal):

    def __init__(self, name):
        #
        self.name = name

#
class Person(object):

    def __init__(self, name):
        #
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

#
class Employee(Person):

    def __init__(self, name, salary):
        # Hmm what kind is this stange magic?
        super(Employee, self).__init__(name)
        # ?
        self.salary = salary

#
class Fish(object):
    pass

#
class Salmon(Fish):
    pass

#
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

#
santa = Cat("Santa")

#
mary = Person("Mary")

#
mary.pet = santa

#
frank = Employee("Frank", 120000)

#
frank.pet = rover

#
flipper = Fish()

#
crouse = Salmon()

#
harry = Halibut()


