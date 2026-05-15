'''
1. Program to convert 24 hr clock into normal clock



time_ = input("Enter 24 hours time format: ")
parts_ = time_.split(":")
hour_ = int(parts_[0])
min_ = int(parts_[1])
if hour_ > 12:
    print(f"{time_} is converted into {hour_ - 12}:{min_} pm")
else:
    print(f"{time_} is converted into {hour_}:{min_} am")

'''
'''
List
----
-->List is a collection of different data type
-->[] and separated by ,
--> mutable

methods
-------
append()
-------
--> this method is used to add new item into list, and it will in the last index position

syntax--> variable_name.append(item)
Immutable
---------
--> Could not able to modify on that particular variable
eg : int, str

mutable
-------
-->Can be able to modify on that particular variable
eg : list

extend()
--------
--> this method is used to add iterable into list, and it will in the last index position, each value or substring is each index in the list
syntax --> variable_name.extend(iterable)

pop()
-----
--> used to remove the item from the list, but will mention here index position in the pop method

syntax--> variable_name.pop(index_position)

remove()
-------
--> used to remove the item from the list, but will mention here direct in the remove method

syntax--> variable_name.remove()
'''
# print p in 3rd class string
any = [1, "Python", [1, 2, [34, "this is python 3rd class", 78], "Python is a language", 89], 34, [3, 4]]
print(any[2][2][1][8])
print(any[2][4])

any = [1, 2, 3]
any.append(6)
print(any)
any.append([20, 90])
print(any)

so = "Python is a"
print(so.replace("Python", "Java"))
print(so)       # strings are immutable
any = [1, 2, 3]
print(any.append(6))   # modify the original list directly and return None to avoid confusion.
print(any)

any = [1, 2, 3]
any.append([4, 5])
print(any)
any.extend([4, 5])
print(any)

any = [1, 2, 3]
any.pop()
print(any)

any = [1, 2, 3]
any.remove(2)
print(any)


so = ["Python", 67, "Java"]
so.remove("Python")
print(so)








