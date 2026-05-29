'''
modules
-------
--> A module in python is a file that contains python code such as
-variables
-functions
-classes
-statements

two types of modules
--------------------
user-define
built-in


import My_module

print(My_module.add(5, 6))

print(My_module.sub(6, 5))

import math
print(math.sqrt(25))
print(math.factorial(10))
print(math.pow(2, 5))

from math import sqrt
print(sqrt(25))

import math as m
print(m.factorial(10))

import os
# os.mkdir("Some_python")
# os.rmdir("Some_python")
# os.remove("meow.txt")

import sys
print(sys.version)
print(sys.path)


import random
print(random.random())
print(random.randint(1000, 9000))

'''

from collections import Counter, defaultdict
data = ['a', 'b', 'c', 'd']
counter = Counter(data)
print(counter)

dd = defaultdict(int)
dd['missing'] += 1
print(dd['missing'])
print(dd)
