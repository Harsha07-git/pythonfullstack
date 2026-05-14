'''

Operators:

1.Arithmetic- +,-,*,/,%,//, **
Example:
print (2*3)
print(4%5==0)
print (10**2)
print (10/2)
print (35.20//5)

2.Assignment- =,+=,-=, %=,*=

Example:
count=0

for j in range (1,10):

count +=1 or on count=count+1

print (count)

3.Comparision
--------------
== -> looks for both are equal or not,
!=,>=, <=,|



4. Logical
-----------
and--> this operator used to check both should be true
or
not

5.Membership
-------------
in
not in

6. Identity
---------------
is --> this operator looks for the object is same or not
is not

7.Bitwise
-----------
&, |, <<, >>

0101
0011
----
0001

'''

print(2*3)
print(4%5 == 0)
print(10**2)
print(10/2)
print(35.20//5)

count = 0
for j in range(1, 10):
    count +=1
print(count)

a = 7
b = 9
print(a == b)

a = [1, 2]
b = [1, 2]
c = a
print(type(a))
print(a == b)
print(id(a))
print(id(b))
print(a is not c)

a = 15
if a % 3 == 0 or a % 5 == 0:
    print("True")

a = 7
b = [1, 2]
print(a not in b)

print(5 | 3)

a = 9 # immutable
b = 7.0
print(a + b)

'''
                                                String
                                                '', "",''''''''
String is sequence of char that are enclosed in '', "", '''''''' and string is immutable

methods
----------
replace()
---------
--> Used to replace with new substring

syntax---> variable_name.replace("old string", "new string")

split()
-------
--> used to separate into parts, and split based on the substring where before substring is one index and after is another index in the list

syntax --> variable_name.split("substring")

len()
------
-->  get the number of items, substring
syntax--> len(variable_name)

slicing()
--------
--> can give access to get particular index from the string.

syntax--> variable_name[starting index : ending index]

indexing()
----------
--> used get substring present in that index position
syntax--> variable_name[index_position]

".".join(vari)

'''

any = "Python78,&"
for j in any:
    print(j)

any = " @&,."
for j in any:
    print(j)

any = "Python is a language"
print(any.replace("Python", "Java"))
print(any)  # show casing the immutable property

print(any.split("a"))
print(any.split("$"))

print(len(any))

print(any[3:11])

print(any[7])

print(any.index("ang"))

any = "P.y.t.h.o.n. .i.s. .a. .l.a.n.g.u.a.g.e."
print(any)



