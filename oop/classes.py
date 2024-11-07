# Simple class definition
class Dog:
  def __init__(self, name) -> None:
    self.name = name
  
  def speak(self):
    print("My name is {}".format(self.name))

obj = Dog("Tommy")
obj.speak()

# Class inheritance - parent class
class Person(object):
  # __init__ is known as the constructor
  def __init__(self, name, idnumber):
    self.name = name
    self.idnumber = idnumber

  def display(self):
    print(self.name)
    print(self.idnumber)
        
  def details(self):
    print("My name is {}".format(self.name))
    print("IdNumber: {}".format(self.idnumber))
    
# Class inheritance - child class
class Employee(Person):
  def __init__(self, name, idnumber, salary, post):
    self.salary = salary
    self.post = post

    # invoking the __init__ of the parent class
    Person.__init__(self, name, idnumber)
        
  def details(self):
    print("My name is {}".format(self.name))
    print("IdNumber: {}".format(self.idnumber))
    print("Post: {}".format(self.post))

# Class polymorphism
class Bird:
  def intro(self):
    print("There are many types of birds.")

  def flight(self):
    print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")

class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

# Encapsulation
class Base:
  def __init__(self):
    self.a = 1    # Public member
    self._b = 2   # Protected member - can be accessed by the class and sub-classes
    self.__c = 3  # Private member - can be accessed only by the class itself

# Abstract class
class Rectangle:
  def __init__(self, length, width):
    self.__length = length  # Private attribute
    self.__width = width    # Private attribute

  def area(self):
    return self.__length * self.__width

  def perimeter(self):
    return 2 * (self.__length + self.__width)