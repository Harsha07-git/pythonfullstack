'''
sets
----
--> A set is a collection of unique and unordered elements
--> Duplicate values are not allowed
--> Items are not stored in index order
--> {}

methods
--------
union()
-------
--> it will give all values from 2 sets together in once

syntax--> variable_name.union(another_variable)

intersection()
--------------
--> to get the common elements from both sets
syntax--> variable_name.intersection(another_variable)

difference()
------------
--> to get the difference values from the set

syntax--> variable_name.difference(another_variable)

add()
-----
--> to add new element into set

syntax--> variable_name.add(element)

update()
--------
--> to add multiple items into set
syntax--> variable_name.update([elements])

remove()
--------

'''
any = {1, 2, 2, 3, 4}
an = {84, 56, 8, 8, 9, 10}
print(any | an)
print(any.union(an))
print(any & an)
print(any.intersection(an))
print(any - an)
print(an.difference(any))

any = {1, 2, 2, 3, 4}
any.add(41)
any.update([41, 90])
print(any)
print(max(any))
print(min(any))

print(len(any))

any = {1, 2, 2, 3, 4}
any.remove(4)
print(any)

any.discard(4)
print(any)
