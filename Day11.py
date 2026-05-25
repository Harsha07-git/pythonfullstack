'''
assert
---------
-->This is debugging statement used to test whether a condition is True

AssertionError


num = 10
assert num >= 18
print("Eligible")

num = 10
assert num >= 18, "Age must be greater than or equal to 18"
print("Eligible")



functions
---------
--> A function is a block of code which only execute when it is called
--> you can pass data, known as parameters into a function
--> To avoid repeated lines in code

def function_name(parameters):
    -----------
    -----------

function_name(arguments)

num = 9
def even(num):
    if num % 2 == 0:
       print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
even(num)
even(109)

Ways to pass arguments
----------------------
1.Required arguments
--------------------
--> A function must be called with the same no of arguments

def even(num, num_2, num_3):
    if num % 2 == 0:
       print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
even(109, 90)

2.Default arguments
-------------------
--> By default, values is defined at parameters even though it will take from arguments

def even(name="Harsha",age=89,sal = 10):
    print(name)
    print(age)
    print(sal)

even("Harshavardhan", 19, 75000)

Keyword arguments
------------------------
--> We can send arguments with key=value syntax. By this, the order of arguments does not
matter.....


def even(name, sal, age):
    print(name)
    print(age)
    print(sal)

even(name="Harsha",age=89,sal = 10)

Variable length arguments
-------------------------
--> Adding a star(*) before the parameter name in the function, receive a tuple of
arguments and can access items with the indexes

def even(*name):
    print(name[3])

even("Harsha","Teja","Sony","Jetlee")

name = "Harsha"
def even(any):
    print(any)
even(name)


def prime_num():
    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(f"{i} is prime")

prime_num()


def palindrome(word):
    empty_str = ""
    for j in word:
        empty_str = j + empty_str
        print(empty_str)
    if empty_str == word:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
        
palindrome(input("Enter a word: "))

'''

def armstrong(num):
    armstrong = 0
    length = len(str(len))
    for i in str(num):
        armstrong += int(i) ** length
    if armstrong == num:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

        
armstrong(int(input("Enter the number: ")))

