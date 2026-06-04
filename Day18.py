'''
OOPS --> Object Oriented Programming System
----

1.class
-------
--> A class is a blueprint or template used to create object

class stu_:
    def edu_(self):
        print("I am studing B.Tech")

    def sports_(self):
        print("cricket")
        print("vall")
        
s1 = stu_()
s1.edu_()
s1.sports_()

2.object
--------
--> An object is an instane of a class
eg:
---

class stu_:
    name = 'Harsha'
s1 = stu_()
print(s1.name)

Attributes
----------
--> Attributes are the variables that belongs to a class or an object

eg:
---
class stu_:
    name = 'Teja'
    age = 46
s1 = stu_()
print(s1.name)
print(s1.age)

methods
-------
--> The functions defined inside the class is methods

class PFS_DA:
    def python(self):
        PFS_DA = 'Batch_03'
        print('This is PFS and DA batch-3')

    def Flask(self):
        PFS = 'Batch_03'
        print('This is for PFS batch-3')

all_ = PFS_DA()
all_.python()
all_.Flask()

Constructor   __init__
-----------
--> A Constructor is a special method that is automatically called when object is created

class ATM:
    def __init__(self, Balance, name):
        self.Balance = Balance
        self.name = name

    def Bal_check(self):
        print(f"The total balance of user {self.name} is {self.Balance + 700}")

    def name_(self):
        print(self.name)

card = ATM(Balance = 5000, name = 'RUSH')
card.Bal_check()
card.name_()

Access Specifiers
-----------------
1. Public
---------
-->This can be accessed from anywhere in the program
2. Protected
------------
--> This is represented using a single underscore(_)
3. Private
----------
This is represented using double underscore(__)

class stu_:
    __name = 'Teja'

s1 = stu_()
print(s1._stu___name)

Encapsulation
-------------
--> Is the process of binding data and methods together

class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def depo_(self, amount):
        self.__balance += amount

    def get_bala(self):
        return self.__balance

acc = Bank(1000)
acc.depo_(10000)
print(acc.get_bala())

'''
