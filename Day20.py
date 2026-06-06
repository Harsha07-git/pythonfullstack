'''
--> When an object is created, this constructor runs automatically.


Polymorphism
------------
--> This means 'many forms' .. it allows the same function, method, or operator to behave
differently depending on the object...

1.Method Overloading
--------------------
--> Method Overloading means defining multiple methods with the same name but different
parameters
eg-1:
-----
class calcu_:
    def add(self, a, b, c=0):
        return a + b + c

an = calcu_()
print(an.add(23,6))
print(an.add(23, 6, 34))

eg-2:
-----
class calcu_:
    def add(self, a, b):  
        return a + b + c
    def add(self, a, b, c=0):
        return a + b + c

an = calcu_()
print(an.add(23,6))
print(an.add(23, 6, 34))

eg-3:
-----
class calcu_:
    def add(self, *num):
        return sum(num)
    
an = calcu_()
print(an.add(23,6))

2.Method Overriding
-------------------
--> This occurs when a child class provides its own implementation of a method already
defined in the parent class...

eg:
---
class animal:
    def sound(self):
        print("Animal makes sound")

class dog(animal):
    def sound(self):
        print("Dog barks")

ntg = dog()
ntg.sound()

3.Operator Overloading
----------------------
--> This allows operators such as +, -, *, etc, to perform different actions for
user-defined objects

note:-
------
--> The operator inside the method will overload a special method or operator given
in the call

__add__
-->This tells Python what to do when + is used between two stu_ objects.

eg-1:
-----
class stu_:
    def __init__(self, marks):
        self.marks = marks
    def __add__(self, other):
        return self.marks + other.marks

an_1 = stu_(4)
an = stu_(78)
print(an_1 + an)

eg-2:
-----
class stu_:
    def __init__(self, marks):
        self.marks = marks
    def __sub__(self, other):
        return self.marks - other.marks

an_1 = stu_(4)
an = stu_(78)
print(an_1 - an)

Data Abstraction
----------------
--> This is the process of hiding internal implementation details and showing only
essential features to the user
--> It focuses on what an object does rather than how it does it...

'''

from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass

class Rec(shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return 2*(self.a * self.b)

an = Rec(10, 5)
print(an.area())
        


