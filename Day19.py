'''
Inheritance
-----------
--> This allows one class to acquire the properties and methods of another class...

Types of Inheritance
--------------------
1.Single Inheritance
--------------------
--> A class inherts from a single parent class...

eg:
---
class father:
    def Land(self):
        print("My Father has 5 Acres of Land")

class Harsha(father):
    def my_own(self):
        print("I have 2 Acres")

fam = Harsha()

fam.Land()

2.Multiple Inheritance
----------------------
--> A class inherts from one or more parent classes...

eg:
---
class father:
    def Land(self):
        print("My Father has 5 Acres of Land")

class mother:
    def gold(self):
        print("My Mother has 1 Kg Gold")

class son(father, mother):
    def mine(self):
        print("I have nothing")

all_ = son()
all_.Land()
all_.gold()

3.Mutli-level Inheritance
-------------------------
--> A class inherts from a parent class and another class inherts from that child class

eg:
---
class grandfather:
    def land(self):
        print("My grandfather have 5 acres of land")

class father(grandfather):
    def flat(self):
        print("I have flat at BNG")

class son(father):
    def Ntg(self):
        print("I own both of their properties")

all_ = son()
all_.land()
all_.flat()
all_.Ntg()

4.Hierarical Inheritance
------------------------
--> Multiple child classes inherts from a single parent...

eg:
---
class father:
    def Land(self):
        print("10 Acres land")

class Harsha(father):
    def mine(self):
        print("Job")

class Harshita(father):
    def sis(self):
        print("Jobless")

har = Harshita()
har.Land()

var = Harsha()
var.Land()

5.Hybrid Inheritance
--------------------
--> This is the combination of two or more types of inheritance

class A:
    def some(self):
        print('Class A')
class B(A):
    def any(self):
        print('Class B')
class C(A):
    def so(self):
        print('Class C')

class D(B, C):
    def All_(self):
        print('Class D')

how = D()
how.so()

super() mathod
--------------
-->super() is used to access methods and constructor of the parent class
from th child class

class parent:
    def display(self):
        print('Method Parent')

class child(parent):
    def display(self):
        super().display()
        print('Method Child')

any = child()
any.display()

'''

class Person:
    def __init__(self, name):
        self.name = name

class stu_(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
    def show(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll}")

any = stu_('Harsha', 41008)
any.show()


