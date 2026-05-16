'''
Concatination
--------------
--> The (+) for int and can add, but for the other data types it will act as concatinating
the data type

Tuple
-----
--> collection of different data types separated by commas, represented in () and
immutable

methods
-------
count()
-------
--> this used to count the particular item in the tuple

syntax--> variable_name.count(item)

index()
-------
--> used to find out the index position of the item and gives first occurence

Dictionary
----------
-->Dict is a key : value pair, key and value separated by : and pair is separated by ,
--> Represented by {}

methods
-------
keys()
------
--> used to get all keys from the dict
syntax--> dict.keys()

values()
--------
--> used to get all the values from the dict

syntax--> dict.values()

update()
--------
--> used to add a new key : value pair to dict

syntax--> dict.update({key:value})

clear()
-------
--> used to remove all the items in the dict

'''

a = 90
b = 8
print(a+b)

any = "Python"
so = "is a language"
print(any+so)

an = [1, 2]
am = [3, 4]
print(an + am)

some = (1, "Python","Python", [1, 2], (3, 4))
print(some[2][1])
print(some.index("Python"))
print(some.count("Python"))

any = (1, "Python", [1, 2, [34, "this is python 3rd class", 78], "Python is a language", 89], 34, [3, 4])
print(any[2][2][1][13])

harsha_details = {"Name": "Harsha",
                  "age": 19,
                  "mobNO": "2943847455",
                  "Pan": "GP73TDV90",
                  1: 2,
                  (1, 2): [3, 4]}
print(type(harsha_details))
print(harsha_details.keys())
print(harsha_details.values())
print(harsha_details.items())

print(harsha_details["Name"])

harsha_details["Aadhar"] = "12345678887654"
# harsha_details.update({"Aadhar":"2753 7196 4653"})
harsha_details["Name"] = "Vardhan"
print(harsha_details)
harsha_details.clear()
print(harsha_details)











